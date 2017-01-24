from collections import deque


class GamePlan(object):

    """
    initialise the tournament object with an overall list of players' IDs

    input:
    a list of players

    output:
    a list (len = number of rounds) of lists of tuples
    with players' names (maybe change to IDs from db) in white, black order

    GamePlans with odd number of players have each person sitting out
    Created as a tuple with ('_BYE', 'real player')
    Template needs to check for '_BYE' in each tuple and
    """

    def __init__(self, players):
        self.players = list(players)

    def berger_robin(self, players):
        """ 
        Input:
              array of player names/ids
        Returns:
              tournament - an array of hashmaps, 
                           each containing matches and bye for the round
        taken from
        https://en.wikipedia.org/wiki/Round-robin_tournament#Scheduling_algorithm
        """
        number_of_players = len(players)
        shift = number_of_players / 2
        last = players.pop()
        pl_deque = deque(players)
        tournament = []
        for stage in xrange(number_of_players - 1):
            round_dict = {'matches': [], 'bye': "__NONE"}
            if last == '_BYE':
                round_dict['bye'] = pl_deque[0]
            else:
                if stage % 2 == 0:
                    round_dict['matches'].append((last, pl_deque[0]))
                else:
                    round_dict['matches'].append((pl_deque[0], last))
            other_games = [(pl_deque[idx], pl_deque[idx + 1])
                           for idx in xrange(1, (len(pl_deque) - 1), 2)]
            round_dict['matches'] += other_games
            tournament.append(round_dict)
            pl_deque.rotate(shift)  # for the next for-loop iteration

        return tournament

    def generate(self):
        players = self.players
        if len(players) % 2 == 1:
            players.append('_BYE')

        return self.berger_robin(players)
