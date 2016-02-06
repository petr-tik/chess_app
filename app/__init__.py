from flask import Flask

app = Flask(__name__)
from app import views
# import at the end, cos app.views needs to import the app variable

