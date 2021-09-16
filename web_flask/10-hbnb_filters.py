#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(self):
    """Close the open storage engine."""
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """Return a page with of State/Amenity filters."""
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State),
                           amenities=storage.all(Amenity))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
