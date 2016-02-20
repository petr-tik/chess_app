import pandas as pd
from collections import namedtuple, deque


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
	
	def berger_robin(self, players):
		n = len(players)
		shift = n/2
		last = players.pop()
		pl_deque = deque(players)
		TOURNAMENT = []
		for x in xrange(n-1):
			matches = []
			if x % 2 == 0:
				matches.append((last, pl_deque[0]))
			else:
				matches.append((pl_deque[0], last))
			other_games = [(pl_deque[x], pl_deque[x+1]) for x in xrange(1,(len(pl_deque)-1), 2)]	

			pl_deque.rotate(shift)	
			TOURNAMENT.append(matches+other_games)

		print TOURNAMENT

	def generate(self):
		if self.system == 'robin':
			if len(self.players) % 2 == 0:
				players = self.players
				return self.berger_robin(players)
			else:
				players = self.players
				players.append('BYE')
				return self.berger_robin(players)

players_even = ['john', 'bob', 'ana']
tourn = Tournament(players_even,'robin')
x = tourn.generate()



		
