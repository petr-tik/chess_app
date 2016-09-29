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

    def __init__(self, PLAYERS):
        self.players = PLAYERS

    def berger_robin(self, players):
    # taken from
    # https://en.wikipedia.org/wiki/Round-robin_tournament#Scheduling_algorithm
        number_of_players = len(players)
        shift = n / 2
        last = players.pop()
        pl_deque = deque(players)
        TOURNAMENT = []
        for x in xrange(number_of_players - 1):
            round_dict = {'matches': [], 'bye': "__NONE"}
            if last == '_BYE':
                round_dict['bye'] = pl_deque[0]
            else:
                if x % 2 == 0:
                    round_dict['matches'].append((last, pl_deque[0]))
                else:
                    round_dict['matches'].append((pl_deque[0], last))
            other_games = [(pl_deque[x], pl_deque[x + 1])
                           for x in xrange(1, (len(pl_deque) - 1), 2)]
            pl_deque.rotate(shift)
            round_dict['matches'] += other_games
            TOURNAMENT.append(round_dict)

        return TOURNAMENT

    def generate(self):
        if len(self.players) % 2 == 0:
            players = self.players
        else:
            players = self.players
            players.append('_BYE')

        return self.berger_robin(players)


