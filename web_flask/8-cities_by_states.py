#!/usr/bin/python3
"""
/states_list: display a HTML page: (inside the tag BODY)
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_context(exception):
    storage.close()


@app.route('/cities_by_states')
def state_route():
    states = storage.all(State)
    all_states = []

    for state in states.values():
        cities = state.cities
        city_list = list(filter(lambda c: c.state_id == state.id, cities))
        city_data = list(map(lambda c: [c.id, c.name], city_list))
        all_states.append([state.id, state.name, city_data])
    return render_template('8-cities_by_states.html', states=all_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
