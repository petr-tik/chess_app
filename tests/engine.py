from hitchserve import ServiceBundle
from os import path, system, chdir
from commandlib import Command, run
from hitchtest import monitor
import hitchselenium
import hitchserve
import hitchpython
import hitchtest


class ExecutionEngine(hitchtest.ExecutionEngine):
    """Python engine for running tests on chess app."""

    def set_up(self):
        """Set up your applications and the test environment."""
        self.path.project = self.path.engine.parent
        self.path.config_file = self.path.project.joinpath("config.py")

        self.path.appdb = self.path.project.joinpath("app.db")
        self.path.testdb = self.path.project.joinpath("test.db")

        if self.path.appdb.exists():
            self.path.appdb.remove()

        if self.path.testdb.exists():
            self.path.testdb.remove()

        self.path.config_file.write_text((
            """import os\n"""
            """basedir = os.path.abspath(os.path.dirname(__file__))\n"""
            """\n"""
            """SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')\n"""
            """SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')\n"""
            """WTF_CSRF_ENABLED = True\n"""
            """SECRET_KEY = 'you-will-never-guess'\n"""
        ))

        self.python_package = hitchpython.PythonPackage(
            python_version=self.settings['python_version']
        )
        self.python_package.build()

        self.python = self.python_package.cmd.python.in_dir(self.path.project)
        self.pip = self.python_package.cmd.pip.in_dir(self.path.project)

        with monitor([self.path.project.joinpath("requirements.txt"), ]) as changed:
            if changed:
                run(self.pip("install", "-r", "requirements.txt"))

        run(Command("bash")("-c", "sqlite3 {0}/test.db < {0}/test.sql".format(self.path.project)))

        #run(self.python("db_create.py"))
        #run(self.python("db_migrate.py"))

        self.services = ServiceBundle(
            project_directory=str(self.path.project),
            startup_timeout=float(self.settings["startup_timeout"]),
            shutdown_timeout=float(self.settings["shutdown_timeout"]),
        )

        # Docs : https://hitchtest.readthedocs.org/en/latest/plugins/hitchpython.html
        self.services['Flask'] = hitchserve.Service(
            command=self.python("run.py"),
            log_line_ready_checker=lambda line: "Restarting with stat" in line,
        )

        # Docs : https://hitchtest.readthedocs.org/en/latest/plugins/hitchselenium.html

        self.services['Firefox'] = hitchselenium.SeleniumService(
            xvfb=self.settings.get("xvfb", False) or self.settings.get("quiet", False),
            no_libfaketime=True,
        )

        self.services.startup(interactive=False)

        # Docs : https://hitchtest.readthedocs.org/en/latest/plugins/hitchselenium.html
        self.driver = self.services['Firefox'].driver

        self.webapp = hitchselenium.SeleniumStepLibrary(
            selenium_webdriver=self.driver,
            wait_for_timeout=5,
        )

        self.click = self.webapp.click
        self.wait_to_appear = self.webapp.wait_to_appear
        self.wait_to_contain = self.webapp.wait_to_contain
        self.wait_for_any_to_contain = self.webapp.wait_for_any_to_contain
        self.click_and_dont_wait_for_page_load = self.webapp.click_and_dont_wait_for_page_load

        # Configure selenium driver
        screen_res = self.settings.get(
            "screen_resolution", {"width": 1024, "height": 768, }
        )
        self.driver.set_window_size(
            int(screen_res['width']), int(screen_res['height'])
        )
        self.driver.set_window_position(0, 0)
        self.driver.implicitly_wait(2.0)
        self.driver.accept_next_alert = True

    def pause(self, message=None):
        """Pause test and launch IPython"""
        if hasattr(self, 'services'):
            self.services.start_interactive_mode()
        self.ipython(message)
        if hasattr(self, 'services'):
            self.services.stop_interactive_mode()

    def load_website(self):
        """Navigate to website in Firefox."""
        self.driver.get("http://localhost:5000")

    def time_travel(self, days=""):
        """Get in the Delorean, Marty!"""
        self.services.time_travel(days=int(days))

    def connect_to_kernel(self, service_name):
        """Connect to IPython kernel embedded in service_name."""
        self.services.connect_to_ipykernel(service_name)

    def on_failure(self):
        """Runs if there is a test failure"""
        if not self.settings['quiet']:
            if self.settings.get("pause_on_failure", False):
                self.pause(message=self.stacktrace.to_template())

    def on_success(self):
        """Runs when a test successfully passes"""
        if self.settings.get("pause_on_success", False):
            self.pause(message="SUCCESS")

    def tear_down(self):
        """Run at the end of all tests."""
        if hasattr(self, 'services'):
            self.services.shutdown()
