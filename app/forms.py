from flask_wtf import Form
from datetime import date
from wtforms import StringField, SelectField, validators, SubmitField, HiddenField
from wtforms.fields.html5 import DateField

	
class CreateTournament(Form):
	tourn_name = StringField('Tournament name', [validators.Length(min=4, max=25)])
	location = StringField('Location')
	date = DateField(format='%d/%m/%Y')
	system = SelectField('Tournament system', choices=[('swiss', 'Swiss system'), ('round_robin', 'Round robin')])
	tie_break = SelectField('Tie breaker', choices=[('head', 'Head to head'), ('black', 'Wins with black')])
	submit = SubmitField("Let's add players")

class AddPlayers(Form):
	name = StringField('Name', [validators.Length(min=4)])
	email = StringField('Email', [validators.Email(message="Insert valid email")])
	submit = SubmitField("Start playing")

class RoundResults(Form):
	# for x in Games:
	outcome = SelectField(choices=[('W','1-0'), ('D', 'Draw'), ('L', '0-1')])
	submit = SubmitField("Next round")
