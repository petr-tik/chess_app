import pandas as pd
from collections import namedtuple

#players = pd.from_csv('players.csv')


class Tournament(object):
	"""
initialise the tournament object with an overall list of players and the system definition (swiss or robin)

input that:


output:
a list of named tuples for each round
where each tuple is of the form 
(['people', 'playing'], 'person sitting out')
Thanks to @DRMacIver


"""
	def __init__(self, PLAYERS, system):
		self.players = PLAYERS
		self.system = system
		self.Round = namedtuple('Round', ('matches', 'bye'))

	def bye(self):
		if len(self.players) % 2 == 0:
			return False
		else:
			return True

	def robin(self):
		# outputs a list of named tuples 
		TOURNAMENT = []
		# number of rounds = number of players - 1 - so everyone plays every other player
		for x in xrange(len(self.players) - 1):
			players = self.players
			matches = []
			while (len(players) > 1):


			else:
				if len(players) == 0:
					bye = 0
				else:
					bye = players[0]


			TOURNAMENT.append(self.Round(matches,bye))

		print TOURNAMENT






"""
>>> Round = namedtuple('Round', ('matches', 'bye'))
>>> x = Round(["stuff"], "someone")
>>> x
Round(matches=['stuff'], bye='someone')
>>> x.matches
['stuff']
>>> x.bye
'someone'
"""


