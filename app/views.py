from __future__ import print_function
from flask import render_template, request, flash, redirect, url_for, g
from app import app, db
from models import Player, Tournament, Game
from forms import CreateTournament, AddPlayers, RoundResults
from datetime import date
import sys
from sqlite3 import dbapi2 as sqlite3
from functools import wraps


DATABASE = 'test.db'

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


@app.route('/', methods=['GET', 'POST'])
def home():
    db = get_db()
    cur = db.execute('SELECT * FROM tournament')
    TOURNS = cur.fetchall()
    if request.method == 'POST':
		if request.form['choice'] == 'Create new':	
			return redirect(url_for("create_tournament"))

		elif request.form['choice'] == 'Load old':
			# go to load pages and pull in all tournament entries from the database
			return redirect(url_for("load_tournament"))
    
    return render_template('index.html', tourns=TOURNS, title="Main menu")


@app.route('/load_tournament', methods = ['GET', 'POST'])
def load_tournament():
    db = get_db()
    cur = db.execute('SELECT id, name FROM tournament')
    TOURNS = cur.fetchall()
    if request.method == 'POST':
        tourn_to_load = request.form['tourn'] # selected tournament
    	return redirect(url_for("add_players"))

    return render_template('load_tournament.html', tourns=TOURNS)


@app.route('/create_tournament', methods = ['GET','POST'])
def create_tournament():
	# page 3
    form = CreateTournament(request.form)
    if request.method == 'POST':
    	nam = request.form['name']
    	loc = request.form['location']
    	cal = request.form['calendar']
    	sys = request.form['system']
    	tie = request.form['tie_break']
    	g.db.execute('''INSERT INTO tournament (id, name, location, calendar, system, tie_break) \
    		VALUES (NULL, ?, ?, ?, ?, ?)''', (nam, loc, cal, sys, tie))
    	return redirect(url_for('add_players'))

    return render_template('create_tournament.html', title='Create new tournament', form=form)

#@app.route('/<tournamentID>/add_players', methods = ['GET', 'POST'])
#def add_players(tournamentID):
@app.route('/add_players', methods = ['GET', 'POST'])
def add_players():
	form = AddPlayers(request.form)
	if request.method == 'POST':
		pass
		
        return redirect(url_for("round"))
    		# else:

	return render_template('add_players.html',form=form)


#@app.route('/<tournamentID>/<round_num>', methods = ['GET', 'POST'])
#def round(tournamentID, round_num):
@app.route('/round', methods = ['GET', 'POST'])
def round():
    """ 
    gets the round number, PLAYERS' names and round match schedule, 
    pass it into the rendered template """
    cur = conn.cursor()
    games = cur.execute("select * from game where \
            game_tournament.tournament_id = ? \
            game.round = ?", tournamentID, round_num).fetchall()
    if request.method == 'POST':
		return redirect(url_for("standings"))
    return render_template('round.html', round_num=round_num, NUM_GAMES=NUM_GAMES, players=players)
    	

#@app.route('/<tournamentID>/<round_num>/standings', methods = ['GET', 'POST'])
#@is_last_round(tournamentID, round_num)
#def standings(tournamentID, round_num):
@app.route('/standings', methods = ['GET', 'POST'])
def standings():
	round_num = 4 # take from the database
	if request.method == 'POST': 
	   return render_template('standings.html', round_num=round_num, PLAYERS=PLAYERS)


