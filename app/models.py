from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(name)

class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
    location = db.Column(db.String)
    date = 
    system = db.Column(db.String) # roundrobin or swiss
    tie_break = db.Column(db.String)  # num won as black or head to head

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.Integer)
    white_id = db.Column(db.Integer)
    black_id = db.Column(db.Integer)
    outcome = db.Column(db.String) # 'W', 'D' or 'L' white reference
    
