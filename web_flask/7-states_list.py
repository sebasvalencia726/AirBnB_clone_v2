#!/usr/bin/python3
"""script that starts a Flask web application:
listening on 0.0.0.0, port 5000
Routes:
    /states_list: display a HTML page: (inside the tag BODY)

"""
from flask import Flask, render_template, g
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage = g.pop('storage', None)

    if storage is not None:
        storage.close()


@app.route('/states_list', strict_slashes=False)
def index():
    """/states_list: display a HTML page: (inside the tag BODY)
    """
    all_states = storage.all(State)
    print(all_states)
    return render_template('7-states_list.html', all_states=all_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
