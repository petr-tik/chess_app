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

	def robin_even(self):
		"""
		Thanks to @eterevsky for reading me rambling on about this, so I could start going the right direction

		"""

		# outputs a list of named tuples 
		TOURNAMENT = []
		# number of rounds = number of players - 1 - so everyone plays every other player
		for x in xrange(len(self.players) - 1):
			players = self.players
			matches = []
			# constantly take the first member of the list
			first = 0

			while players:
				#make a pair
				other = 1
				potential_pair = (players[first], players[other])
				if any(potential_pair in mat for mat in TOURNAMENT):
					other += 1
					continue
				else:
					# append them to matches for the round
					matches.append(potential_pair)
					#delete them from players
					players = [pl for pl in players if pl not in potential_pair]
					continue
				
			bye = []
			TOURNAMENT.append(matches)
			print TOURNAMENT[x]
		print TOURNAMENT


	def robin_odd(self):
		pass

	def generate(self):
		if self.system == 'robin':
			if self.bye():
				self.robin_odd()
			else:
				self.robin_even()
		else:
			pass




even_lads = ['bob', 'john', 'max', 'adam']
tourn = Tournament(even_lads, 'robin')
tourn.generate()



