#!/usr/bin/python3
"""
    displays the results of states and amenities to a web page
    via "/hbnb_filters" route
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_context(exception):
    """
        deletes data from previous session
    """
    storage.close()


@app.route("/hbnb_filters")
def states_cities_route():
    """
        Route that fetches all cities in a stage
        from the storage engine
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    all_states = []
    all_amenities = []

    for state in states.values():
        cities = state.cities
        city_list = list(filter(lambda x: x.state_id == state.id, cities))
        c_data = list(map(lambda x: [x.id, x.name], city_list))
        all_states.append([state.id, state.name, c_data])
    for amenity in amenities.values():
        all_amenities.append([amenity.id, amenity.name])

    return render_template("10-hbnb_filters.html", states=all_states,
                           amenities=all_amenities
                           )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
