import pandas as pd
from collections import namedtuple, deque

#players = pd.from_csv('players.csv')


def before(LoL, element):
	# takes List of lists and element, returns boolean
	# a function that checks if element of its mirror opposite has appeared before
	flatL = [x for sublist in LoL for x in sublist]
	if element not in flatL and element[::-1] not in flatL:
		return False
	else:
		return True


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

	def round_robin_even(self, players, TOURNAMENT):
		"""
		Thanks to @eterevsky for reading me rambling on about this, so I could start going the right direction

		"""
		matches = []
		# constantly take the first member of the list
		first = 0
		other = 1
		while players:
			print "Matches scheduled for this round:", matches
			print "The players still available:", players
			#make a pair				
			potential_pair = (players[first], players[other])
			print "Potential pair:", potential_pair
			print "Matches scheduled until now:", TOURNAMENT
			if before(TOURNAMENT, potential_pair):
				#or (potential_pair[::-1] in sublist for sublist in TOURNAMENT)
				print "potential pair {} was found in {}".format(potential_pair, TOURNAMENT)
				other += 1
				continue
			else:
				print "\n\n\n{} is a new pair and I will add them to {}".format(potential_pair, matches)

				# append them to matches for the round
				matches.append(potential_pair)
				#delete them from players
				players = [pl for pl in players if pl not in potential_pair]
				other = 1
					
				
		return matches	

	def berger_robin_even(self):
		players = self.players
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

		return TOURNAMENT


	def full_robin_even(self):
		TOURNAMENT = []
		for x in xrange(len(self.players) - 1):
			matches = self.round_robin_even(self.players, TOURNAMENT)
			TOURNAMENT.append(matches)

		print TOURNAMENT



	def robin_odd(self, players):
		players = self.players
		matches = []
		bye = []
		for pl in players:
			bye.append(pl)
			left_players = [x for x in players if x != pl]
			self.robin_even(self)


	def generate(self):
		if self.system == 'robin':
			if self.bye():
				self.robin_odd(self)
			else:
				self.berger_robin_even()
		elif self.system == 'swiss':
			pass




even_lads = ['bob', 'john', 'max', 'adam', 'chris', 'ana']
odd_lads = ['bob', 'john', 'max', 'adam', 'chris']
tourn = Tournament(even_lads, 'robin')
tourn.generate()



