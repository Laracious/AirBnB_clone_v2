#!/usr/bin/python3
""" This script starts a web application for the HBNB project"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def remove(exception):
    """ closes the current session """

    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb():
    """ Configures the hbnb filters route """

    states = storage.all("State")
    amenities = storage.all("Amenity")

    states_arr = []
    for state in states.values():
        state_dict = {}
        state_dict["id"] = state.id
        state_dict["name"] 
