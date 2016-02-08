from flask_wtf import Form
from datetime import date
from wtforms import StringField, SelectField, validators, SubmitField, HiddenField, DateTimeField


class ChooseTournament(Form):
	which = SelectField('New tournament', choices=[('load', 'load'), ('create', 'create')])

class CreateTournament(Form):
	tourn_name = StringField('Tournament name', [validators.Length(min=4, max=25)])
	system = SelectField('Tournament system', choices=[('Swiss', 'Swiss'), ('Round robin', 'Round robin')])
	tie_break = SelectField('Tie breaker', choices=[('Swiss', 'Swiss'), ('Round robin', 'Round robin')])
	location = StringField('Location')
	date = DateTimeField(format='%d/%m/%Y', default="{:%d/%m/%Y}".format(date.today()))
	submit = SubmitField("Create tournament")


class AddPlayers(Form):
	name = StringField('Name', [validators.Length(min=4)])
	email = StringField('Email', [validators.Email(message="Insert valid email")])
	submit = SubmitField("Start playing")


class RoundResults(Form):
	# for x in Games:
	outcome = SelectField(choices=[('W','1-0'), ('D', 'Draw'), ('L', '0-1')])