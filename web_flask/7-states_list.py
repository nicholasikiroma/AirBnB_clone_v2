#!/usr/bin/python3
"""states_list: display a HTML page: (inside the tag BODY)"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_context(exception):
    """Handles clean up"""
    storage.close()


@app.route('/states_list')
def state_route():
    """lists all states"""
    return render_template('7-states_list.html',
                            states=storage.all(state))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
