#!/usr/bin/python3
""" The simple web application that start a websrver
    based on flask framework
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns the hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB test """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ returns the custom text """
    return f"C {text}"


@app.route('/python', defaults={"text": "is cool"})
@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>')
def python(text):
    """ return the custom text """
    if len(text) == 0:
        return "Python is cool"
    else:
        text = text.replace('-', " ")
        return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
