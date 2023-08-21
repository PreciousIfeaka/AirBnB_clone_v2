#!/usr/bin/python3
"""This script starts a Flask web app and makes it listen on
0.0.0.0, port 5000. Also rounting to / to display Hello HBNB!
"""

from flask import Flask

app = Flask(__name__)  # creates an instance of the Flask class


@app.route("/", strict_slashes=False)
def hello():
    return "<p>Hello HBNB!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
