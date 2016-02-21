import unittest
from planner import Tournament

class testTournament(unittest.TestCase):
	def setUp(self):
		players_odd = ['john', 'bob', 'ana', 'kate', 'paolo', 'peter', 'jae', 'harry', 'will']
		players_even = ['john', 'bob', 'ana', 'kate', 'paolo', 'peter', 'jae', 'harry']
		self.tourn_odd_robin = Tournament(players_odd,'robin')
		self.tourn_even_robin = Tournament(players_even,'robin')
		self.Rounds_even = self.tourn_even_robin.generate()

	def test_players_per_round(self):
		# test that each round only has max number of players not more than double the number of couples
		for rnd in self.Rounds_even:
			self.assertTrue(len(self.tourn_even_robin.players) <= 2*len(rnd))

	def test_everyone_plays(self):
		for rnd in self.Rounds_even:
			pass			

if __name__ == '__main__':
    unittest.main(verbosity=10)

		