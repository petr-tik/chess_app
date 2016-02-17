import pandas as pd


#players = pd.from_csv('players.csv')


class Tournament(object):
	"""
initialise the tournament object with an overall list of players and the system definition (swiss or robin)

input that:


output:
a named tuple with a list of matches and a bye person
Thanks to @DRMacIver


"""
	def __init__(self, PLAYERS, system):
		self.players = PLAYERS
		self.system = system

	def bye(self):
		if len(self.players) % 2 == 0:
			return False
		else:
			return True

	


