from flask import render_template, request, flash, redirect, url_for, validate_on_submit
from app import app, db
from models import Player, Tournament, Game
from forms import CreateTournament, AddPlayers, RoundResults
from datetime import date
import sys


@app.route('/', methods=['GET', 'POST'])
def home():
	tourns = Tournament.query.all()
	if request.method == 'POST':
		if request.form['choice'] == 'Create new':	
			return redirect(url_for("create_tournament"))
		elif request.form['choice'] == 'Load old':
			# go to load pages and pull in all tournament entries from the database
			return redirect(url_for("load_tournament"))
	return render_template('index.html', tourns=tourns, title="Choose")


@app.route('/load_tournament', methods = ['GET', 'POST'])
def load_tournament():
	# connect to database and list all tournaments by name
	tourns = Tournament.query.all()
	if request.method == 'POST':
		tourn_to_load = request.form['tourn'] # selected tournament

		# any tournament can be live or registering. 
		# if live - player registration closed. find the latest round without results 
		# elif registering - you can still add players and start playing
		return redirect(url_for("add_players"))

	return render_template('load_tournament.html', tourns=tourns)
	# submit button load 

@app.route('/create_tournament', methods = ['GET','POST'])
def create_tournament():
	# page 3
    form = CreateTournament(request.form)
    if form.validate_on_submit():
    	sys.stderr.write(request.form['tourn_name']+"\n")
    	sys.stderr.write(request.form['location']+"\n")
    	sys.stderr.write(request.form['date']+"\n")
    	sys.stderr.write(request.form['system']+"\n")
    	sys.stderr.write(request.form['tie_break']+"\n")
#    	db.session.add(torn)
#   	db.session.commit()
    	return redirect(url_for('add_players'))

    return render_template('create_tournament.html', title='Create new tournament', form=form)


#@app.route('/<tournamentID>/add_players', methods = ['GET', 'POST'])
#def add_players(tournamentID):
@app.route('/add_players', methods = ['GET', 'POST'])
def add_players():
	form = AddPlayers(request.form)
	if request.method == 'POST':
		if request.form['send'] == 'Add player':
			new = (request.form['name'], request.form['email'])
			PLAYERS.append(new)
			#db.session.add(new)

		elif request.form['send'] == 'Delete':
			pass
			# delete that row in the table
			# delete the entry from db.session


		elif request.form['send'] == 'Start playing':
			# flash a window asking user to confirm selection
			# "Are you sure? You cannot add players once you start!""
			# if yes

				#db.session.commit() 
				#return redirect(url_for("round"))
			return redirect(url_for("round"))
			# else:

	return render_template('add_players.html',form=form)
	


#@app.route('/<tournamentID>/<round_c>', methods = ['GET', 'POST'])
#def round(tournamentID, round_c):
# <round_c> will be passed in as variable
@app.route('/round', methods = ['GET', 'POST'])
def round():
	"""gets the round number, PLAYERS' names and round match schedule, pass it into the rendered template 

	make a template to enter results and proceed to the next round """

	round_c = 4 # take from the database
	players = ['bob', 'john', 'colin', 'adam', 'ana', 'petr'] # need a list of names, where opponents are 2 
	# a global number of games per round, that will be calculated for each tournament 
	NUM_GAMES = len(players)

	if request.method == 'POST':
		return redirect(url_for("standings"))

	return render_template('round.html', round_c=round_c, NUM_GAMES=NUM_GAMES, players=players)
    	

#@app.route('/<tournamentID>/<round_c>/standings', methods = ['GET', 'POST'])
#def standings(tournamentID, round_c):
@app.route('/standings', methods = ['GET', 'POST'])
def standings():
	round_c = 4 # take from the database
	NUM_ROUNDS = 5
	if request.method == 'POST':
		if request.form['button'] == "Final result":
			return redirect(url_for('final'))
	return render_template('standings.html', round_c=round_c, NUM_ROUNDS=NUM_ROUNDS, PLAYERS=PLAYERS)


@app.route('/final_results', methods = ['GET', 'POST'])
def final_results():
	if request.method == 'POST':
		# send email to all participants with final standings and round results 
		pass


	return render_template('final_results.html', PLAYERS = PLAYERS, winner = 'john')
