import unittest
from planner import Tournament

class testTournament(unittest.TestCase):
	def setUp(self):
		players_odd = ['john', 'bob', 'ana', 'kate', 'paolo', 'peter', 'jae', 'harry', 'will']
		players_even = ['john', 'bob', 'ana', 'kate', 'paolo', 'peter', 'jae', 'harry']
		self.tourn_odd_robin = Tournament(players_odd,'robin')
		self.tourn_odd_swiss = Tournament(players_odd,'swiss')
		self.tourn_even_robin = Tournament(players_even,'robin')
		self.tourn_even_swiss = Tournament(players_even,'swiss')


	def everyone_plays(self):
		


	def test_three_in_a_row(self):
		x = self.tourn_even_robin.berger_robin_even()
		
		for player in self.tourn_even_robin.players:
			# in all matches no player plays the same colour more than twice in a row




if __name__ == '__main__':
    unittest.main(verbosity=10)

		