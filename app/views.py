from flask import render_template, request, flash, redirect, url_for
from app import app
from models import Player, Tournament, Game
from forms import ChooseTournament, CreateTournament, AddPlayers, RoundResults
from json import dumps
import sys

@app.route('/', methods = ['GET', 'POST'])
def home():
	# page 1
	form = ChooseTournament(request.form)
	sys.stderr.write("got the form\n")
		
	if request.method == 'POST':
		sys.stderr.write("post request received\n")
		if request.form['answer'] == 'create':
			sys.stderr.write(request.form['answer'])

			pass
			# go to the create page
		elif request.form['answer'] == 'load':
			# go to load pages and pull in all tournament entries from the database
			sys.stderr.write(request.form['answer'])

			pass

	return render_template('index.html', form=form, title="Choose")


@app.route('/load_tournament', methods = ['GET', 'POST'])
def load():
	# page 2
	# connect to database and list all tournaments by name
	


	# submit button load 



@app.route('/create_tournament', methods = ['GET','POST'])
def create():
	# page 3
    form = CreateTournament(request.form)
    #if request.method == 'POST' and form.validate():
    return render_template('create_tournament.html', title='Home',form=form)



@app.route('/add_players', methods = ['GET', 'POST'])
def add_players():
	form = AddPlayers(request.form)

	return render_template('add_players.html',form=form)
	
	if request.method == 'POST' and form.validate_on_submit():
		print dumps(form)

@app.route('/round', methods = ['GET', 'POST'])
def round():
	round_c = 4 # take from the database
	names = ['bob', 'john', 'colin', 'adam', 'ana', 'petr'] # need a list of names, where opponents are 2 

	# a global number of games per round, that will be calculated for each tournament 
	NUM_GAMES = len(names)/2
	choices = ['1-0', 'Draw', '0-1']
	return render_template('round.html', round_c=round_c, NUM_GAMES=NUM_GAMES, names=names, choices=choices)
    	


@app.route('/standings', methods = ['GET', 'POST'])
def generate_table():

	"""gets the round number, players names and round match schedule, pass it into the rendered template 

	make a template to enter results and proceed to the next round """
	round_c = 4 # take from the database
	form = RoundResults(request.form)
	names = ['bob', 'john', 'colin', 'adam', 'ana', 'petr'] # need a list of names, where opponents are 2 

	# a global number of games per round, that will be calculated for each tournament 
	NUM_GAMES = len(names)/2

	return render_template('standings.html', round_c=round_c, form=form, NUM_GAMES=NUM_GAMES, names=names)