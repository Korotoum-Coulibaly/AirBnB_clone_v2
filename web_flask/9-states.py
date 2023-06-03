#!/usr/bin/python3
""" script that starts a Flask web application """
from os import getenv
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Function that close session after each request"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ Function that display the list of cities of the states in order"""
    states = storage.all(State).values()
    if id is not None:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', states=state)
        return render_template('9-states.html')
    return render_template('9-states.html', states=states, full=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
