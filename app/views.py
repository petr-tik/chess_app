from flask import render_template, request, flash, redirect, url_for
from app import app
from models import Player, Tournament, Game
from forms import ChooseTournament, CreateTournament, AddPlayers, RoundResults

@app.route('/', methods = ['GET', 'POST'])
def home():
	form = ChooseTournament(request.form)
	if form.validate_on_submit():
		if 'create' in request.form:
			return redirect(url_for('create_tournament'))
		elif 'load' in request.form:
			return redirect(url_for('load_tournament'))
	
	return render_template('index.html')




@app.route('/create_tournament', methods = ['GET','POST'])
def create():
    #form = CreateTournament(request.form)
    #if request.method == 'POST' and form.validate():
    	u	


    #	return 
	return render_template('create_tournament.html', title='Home')

