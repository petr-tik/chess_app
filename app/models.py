from app import db

class Player(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(name)

class Tournament(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    location = db.Column(db.String(32))
    system = db.Column(db.String(32)) # roundrobin or swiss
    tie_break = db.Column(db.String(32))  # num won as black or head to head
    
    def __repr__(self):
        return '<Tournament {}>'.format(name)    

class Game(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.Integer)
    white_id = db.Column(db.Integer)
    black_id = db.Column(db.Integer)
    outcome = db.Column(db.String(10)) # 'W', 'D' or 'L' white reference

    def __repr__(self):
        return '<Game {}>'.format(ID)    
