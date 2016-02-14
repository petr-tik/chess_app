from flask_wtf import Form
from datetime import date
from wtforms import StringField, SelectField, validators, SubmitField, HiddenField, DateTimeField


class ChooseTournament(Form):
	choice = SelectField('New tournament', choices=[('load', 'load'), ('create', 'create')])
	
class CreateTournament(Form):
	tourn_name = StringField('Tournament name', [validators.Length(min=4, max=25)])
	system = SelectField('Tournament system', choices=[('swiss', 'Swiss'), ('round_robin', 'Round robin')])
	tie_break = SelectField('Tie breaker', choices=[('head', 'Head to head'), ('black', 'Black wins')])
	location = StringField('Location')
	date = DateTimeField(format='%d/%m/%Y')
	submit = SubmitField("Let's add players")


class AddPlayers(Form):
	name = StringField('Name', [validators.Length(min=4)])
	email = StringField('Email', [validators.Email(message="Insert valid email")])
	submit = SubmitField("Start playing")


class RoundResults(Form):
	# for x in Games:
	outcome = SelectField(choices=[('W','1-0'), ('D', 'Draw'), ('L', '0-1')])
	submit = SubmitField("Next round")