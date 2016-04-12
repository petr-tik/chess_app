import unittest
from planner import GamePlan

class testTournament(unittest.TestCase):
	def setUp(self):
		self.players_odd = ['john', 'bob', 'ana', 'kate', 'paolo', 'peter', 'Joe', 'Fred', 'Mike', 'Em', 'Theo']
		self.players_even = ['john', 'bob', 'ana', 'kate', 'paolo', 'peter', 'Joe', 'Fred', 'Mike']
		self.tourn_odd_robin = GamePlan(self.players_odd)
		self.tourn_even_robin = GamePlan(self.players_even)
		self.rounds_even = self.tourn_even_robin.generate()
		self.rounds_odd = self.tourn_odd_robin.generate()

	def test_players_per_round(self):
		# test that each round only has max number of players not more than double the number of couples
		for rnd in self.rounds_even:
			self.assertTrue(len(self.tourn_even_robin.players) <= 2*len(rnd))

	def test_everyone_plays_even(self):
		# everyone must play in each round
		for rnd in self.rounds_even:
			for player in self.players_even:
				self.assertTrue(player in tup_rnd for tup_rnd in rnd)

	def test_everyone_plays_odd(self):
		# everyone must play in each round
		for rnd in self.rounds_odd:
			for player in self.players_odd:
				self.assertTrue(player in tup_rnd for tup_rnd in rnd)

	def test_everyone_bye(self):
		tup_byes = []
		for rnd in self.rounds_odd:
			for tup_rnd in rnd:
				if '_BYE' in tup_rnd:
					tup_byes.append(tup_rnd)
			byes = [player in tup for tup in tup_byes if player != '_BYE']
			# everyone should sit out once and only once
			self.assertEqual(sorted(self.players_odd), sorted(byes))

if __name__ == '__main__':
    unittest.main(verbosity=10)

		
