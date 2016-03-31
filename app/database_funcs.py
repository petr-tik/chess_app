#!/usr/bin/env python

from functools import wraps

# DATABASE INTERACTION FUNCTIONS

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# Wrapper func to return different last page of standings

def is_last_round(func):
    def decorator(f):
        @wraps(func)
        def decorated_function(*args, *kwargs):
            # get the max round value and check if round_num is last round

            if round_num == final_round:
                return render_template('final_results.html')
            else:
                return render_template('standings.html', round_num=round_num)



        return decorated_function
    return decorator


