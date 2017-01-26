import unittest
from src.planner import GamePlan
import pdb


class testTournament(unittest.TestCase):

    def setUp(self):
        # NAMES = ['john', 'bob', 'generic_name', 'kate', 'paolo',
        #          'peter', "Joe", 'Fred', 'Mike', 'Em', 'Theo']
        NAMES = list(xrange(150))  # use int ids instead
        self.players_even = [NAMES[idx] for idx in xrange(10)]
        self.players_odd = [NAMES[idx] for idx in xrange(11)]
        self.tourn_odd_robin = GamePlan(self.players_odd)
        self.tourn_even_robin = GamePlan(self.players_even)
        self.rounds_even = self.tourn_even_robin.generate()
        self.rounds_odd = self.tourn_odd_robin.generate()

    def test_odd_is_odd(self):
        self.assertTrue(len(self.players_odd) % 2 == 1)

    def test_even_is_even(self):
        self.assertTrue(len(self.players_even) % 2 == 0)

    def test_players_per_round(self):
        """test that each round only has max number of players not more than
        double the number of couples"""
        for rnd in self.rounds_even:
            self.assertTrue(
                len(self.tourn_even_robin.players) <= 2 * len(rnd['matches']))

    def test_everyone_plays_even(self):
        """ Test that everyone plays in each round with even player numbers"""
        for rnd in self.rounds_even:
            for player in self.players_even:
                self.assertTrue(player in tup_rnd for tup_rnd in rnd)

    def test_everyone_plays_odd(self):
        """ In an odd-player tournament, each player plays each round """
        for rnd in self.rounds_odd:
            for player in self.players_odd:
                self.assertTrue(player in tup_rnd for tup_rnd in rnd)

    def test_everyone_bye(self):
        """ In an odd-player tournament, each player sits out"""
        byes = []  # list of players who sit out
        for rnd in self.rounds_odd:
            byes.append(rnd['bye'])
        # should sit out once and only once
        self.assertEqual(sorted(self.players_odd), sorted(byes))

    def test_everyone_plays_everyone_even(self):
        """ Each player plays 1 and only 1 match against another """

        pass

if __name__ == '__main__':
    unittest.main(verbosity=10)
