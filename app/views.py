from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_tournament')
def index():
    return render_template('create_tournament.html', title='Home')

