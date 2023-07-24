#!/usr/bin/python3
""" The simple web application that start a websrver
    based on flask framework
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns hello HBNB text """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return the HBNB text """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ return the custom text """
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
