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


	def test_bye(self):
		self.assertEqual(True, self.tourn_odd_robin.bye())
		self.assertEqual(True, self.tourn_odd_swiss.bye())
		self.assertEqual(False, self.tourn_even_robin.bye())
		self.assertEqual(False, self.tourn_even_swiss.bye())

	def test_three_in_a_row(self):
		pass

	def test_round(self):
		# all players paired up 
		self.assertEqual(2*len(self.Round.matches) + len(self.Round.bye), len(self.players))












if __name__ == '__main__':
    unittest.main(verbosity=10)

		