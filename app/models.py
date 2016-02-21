from app import db

class Player(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Player {}>'.format(self.name)

class Tournament(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    location = db.Column(db.String(32))
    date = db.Column(db.DateTime)
    system = db.Column(db.String(32)) # roundrobin or swiss
    tie_break = db.Column(db.String(32))  # num won as black or head to head
    
    def __init__(self, name, location, system, tie_break):
        self.name = name
        self.location = location
        self.date = date
        self.system = system
        self.tie_break = tie_break

    def __repr__(self):
        return '<Tournament {}>'.format(self.name)    

class Game(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    TournamentID = db.Column(db.Integer) # pull in from tournament database
    round_num = db.Column(db.Integer)
    white_id = db.Column(db.Integer)
    black_id = db.Column(db.Integer) # pull players' IDs from Player db
    outcome = db.Column(db.String(10)) # 'W', 'D' or 'L' white reference

    def __repr__(self):
        return '<Game {}>'.format(self.ID)    

