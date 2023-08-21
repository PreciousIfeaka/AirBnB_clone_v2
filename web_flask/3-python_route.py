#!/usr/bin/python3
"""This script starts a flask web app using 3 different routes
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


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return "C " + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_is_cool(text="is cool"):
    return "Python " + text.replace('_', ' ')

if __name__ == "__main__":
    """runs the functions"""
    app.run(host='0.0.0.0', port=5000)
