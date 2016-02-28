from app import db
"""
create a tournament and make a database entry, save tournament ID in cookies session.
add players from the table once it's been submitted. 

For round robin, make a schedule of games,
"""

class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    location = db.Column(db.String(32))
    date = db.Column(db.DateTime)
    system = db.Column(db.String(10)) # roundrobin or swiss
    tie_break = db.Column(db.String(10))  # num won as black or head to head
    games = db.relationship('Game', backref = 'tournament', lazy = 'dynamic')

    def __init__(self, name, location, date, system, tie_break):
        self.name = name
        self.location = location
        self.date = date
        self.system = system
        self.tie_break = tie_break

    def __repr__(self):
        return '<Tournament {}>'.format(self.name)    

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Player {}>'.format(self.name)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # pull in from tournament database
    TournamentID = db.Column(db.Integer, db.ForeignKey('tournament.id')) 
    round_num = db.Column(db.Integer)
    # pull players' IDs from Player db
    white_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    black_id = db.Column(db.Integer, db.ForeignKey('player.id')) 
    outcome = db.Column(db.String(5)) # 'W', 'D' or 'L' white reference

    def __init__(self, TournamentID, round_num, white_id, black_id, outcome=None):
        self.TournamentID = TournamentID # pull in from Tournament info
        self.round_num = round_num
        self.white_id = white_id
        self.black_id = black_id
        if outcome:
            self.outcome = outcome

    def __repr__(self):
        return '<Game {}>'.format(self.ID)    

