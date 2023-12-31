#!/usr/bin/python3
"""starts a flask web application
"""

from os import environ
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """removes the current SQLAlchemy session
    """

    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=""):
    """displays a HTML page with a list of cities by states

    Return:
        return an html template redering a list of cities by states
    """

    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    found = 0
    state = ""
    cities = []

    for i in states:
        if id == i.id:
            state = i
            found = 1
            break
    if found:
        states = sorted(state.cities, key=lambda k: k.name)
        state = state.name

    if id and not found:
        found = 2

    return render_template('9-states.html',
                           state=state,
                           array=states,
                           found=found)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
