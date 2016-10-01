from __future__ import print_function
from flask import render_template, request, flash, redirect, url_for, g
from app import app, db
from models import Player, Tournament, Game
from forms import CreateTournament, AddPlayers, RoundResults
from datetime import date
import sys
from sqlite3 import dbapi2 as sqlite3
from functools import wraps

#

# Database interaction       #

#

DATABASE = 'test2.db'


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, '_database'):
        g._database = connect_db()
    return g._database


#

# Custom decorators          #

#


@app.teardown_appcontext
def close_db(error):
    """Commits again and closes the database when app context ends."""
    if hasattr(g, '_database'):
        g._database.close()


@app.teardown_request
def teardown_request(exception):
    """Commits again and closes the database again at the end of the request."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


#

# Routes                 #

#


@app.route('/', methods=['GET', 'POST'])
def home():
    db = get_db()
    cur = db.execute('SELECT * FROM tournament')
    TOURNS = cur.fetchall()
    if request.method == 'POST':
        if request.form['choice'] == 'Create new':
            return redirect(url_for("create_tournament"))

        elif request.form['choice'] == 'Load old':
            # go to load pages and pull in all tournament entries from the
            # database
            return redirect(url_for("load_tournament"))
    db.close()
    return render_template('index.html', tourns=TOURNS, title="Main menu")


@app.route('/load_tournament', methods=['GET', 'POST'])
def load_tournament():
    db = get_db()
    cur = db.execute('SELECT id, name, round_num FROM tournament')
    TOURNS = cur.fetchall()
    db.close()
    if request.method == 'POST':
        tourn_to_load = request.form['tourn']
        return redirect(url_for("round", tournamentID=tourn_to_load, round_num=2))

    return render_template('load_tournament.html', tourns=TOURNS)


@app.route('/create_tournament', methods=['GET', 'POST'])
def create_tournament():
    form = CreateTournament(request.form)
    db = get_db()
    if request.method == 'POST':
        nam = request.form['tourn_name']
        loc = request.form['location']
        cal = request.form['calendar']
        sys = request.form['system']
        tie = request.form['tie_break']
        db.execute('''INSERT INTO tournament \
			(id, name, location, calendar, system, tie_break, round_num) \
			VALUES (NULL, ?, ?, ?, ?, ?, ?)''', (nam, loc, cal, sys, tie, 1))
        db.commit()
        tournamentID = str(
            db.execute('''SELECT max(id) FROM tournament''').fetchone()[0])
        db.close()
        return redirect(url_for('add_players', tournamentID=tournamentID))

    return render_template('create_tournament.html', title='Create new tournament', form=form)


@app.route('/<tournamentID>/add_players', methods=['GET', 'POST'])
def add_players(tournamentID):
    form = AddPlayers(request.form)
    db = get_db()
    if request.method == 'POST':
        db.close()
        return redirect(url_for("round", tournamentID=tournamentID, round_num=1))
    return render_template('add_players.html', form=form)

""" for player in players:
				db.execute('''INSERT INTO player (id, name, email) \
				VALUES (NULL, ?, ?), (player[0], player[1])''')
				latest_player_id = db.execute('''SELECT max(id) FROM player''').fetchone()[0]
				db.execute('''INSERT INTO player_tournament (player_id, tournament_id) \
					VALUES (?, ?)''', (latest_player_id, tournamentID))
				db.commit()
"""

#@is_last_round(tournamentID, round_num)


@app.route('/<tournamentID>/round_<round_num>', methods=['GET', 'POST'])
def round(tournamentID, round_num):
    """
    gets the round number, PLAYERS' names and round match schedule,
    pass it into the rendered template """
    db = get_db()
    cur = db.execute('''select * from game, game_tournament WHERE \
			game_tournament.tournament_id = ? AND \
			game.round_num = ?''', (tournamentID, round_num))

    games = cur.fetchall()
    if request.method == 'POST':
        return redirect(url_for("standings"))
    return render_template('test.html', games=games)


#@app.route('/<tournamentID>/<round_num>/standings', methods = ['GET', 'POST'])
#@is_last_round(tournamentID, round_num)
# def standings(tournamentID, round_num):
@app.route('/standings', methods=['GET', 'POST'])
def standings():
    round_num = 4  # take from the database
    if request.method == 'POST':
        return render_template('standings.html', round_num=round_num, PLAYERS=PLAYERS)
