#!/usr/bin/python3
"""starts a flask web application
"""

from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """displays a HTML page with a list of states

    Return:
        return an html template
    """

    states = storage.all(State)

    return render_template('7-states_list.html')

@app.teardown_appcontext
def close_db(error):
    """remove the current SQLAlchemy session
    """

    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
