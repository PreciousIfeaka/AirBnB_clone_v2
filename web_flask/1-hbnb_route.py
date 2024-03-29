#!/usr/bin/python3
"""This script starts a flask web app using different routes
to print different text
"""

from flask import Flask


app = Flask(__name__)  # creates an instance of Flask class


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    """runs the functions"""
    app.run(host='0.0.0.0', port=5000)
