#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(self):
    """Close the open storage engine."""
    storage.close()


@app.route('/states')
def states():
    """Return a page of all `States`."""
    return render_template('9-states.html', all_states=storage.all(State))


@app.route('/states/<id>')
def states_ids(id):
    """Displays html for states and id"""
    try:
        state = storage.all(State)["State.{}".format(id)]
        return render_template('9-states.html', state=state)
    except KeyError:
        return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
