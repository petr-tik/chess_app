from flask import render_template, request, flash, redirect, url_for
from app import app
from models import Player, Tournament, Game
from forms import ChooseTournament, CreateTournament, AddPlayers, RoundResults

@app.route('/', methods = ['GET', 'POST'])
def home():
	form = ChooseTournament(request.form)
	if form.validate_on_submit():
		if request.form['create']:
			return redirect('create')
		elif request.form['load']:
			return redirect(url_for('load_tournament'))
	
	return render_template('index.html', form=form, title="Choose")




@app.route('/create', methods = ['GET','POST'])
def create():
    form = CreateTournament(request.form)
    #if request.method == 'POST' and form.validate():
    return render_template('create_tournament.html', title='Home',form=form)



@app.route('/add_players', methods = ['GET', 'POST'])
def add_players():
	form = AddPlayers(request.form)



	return render_template('add_players.html',form=form)


@app.route('/standings', methods = ['GET', 'POST'])
def generate_table():
	num_rounds = 5 # take from the database

	return render_template('standings.html', num_rounds=num_rounds)