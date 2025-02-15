#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Function that close session after each request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Function thatdisplay the list of the states in the database"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
