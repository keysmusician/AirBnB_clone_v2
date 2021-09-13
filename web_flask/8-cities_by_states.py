#!/usr/bin/python3
"""This script starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """Close the open file storage engine."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_states():
    """Return a page of all `Sates`, sorted."""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
