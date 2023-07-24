#!/usr/bin/python3
""" The simple web application that start a websrver
    based on flask framework
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns 'Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ Returns the custom text """
    return f"C {text}"


@app.route('/python', defaults={"text": "is cool"})
@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>')
def python(text):
    """ returns the custom text """
    if len(text) == 0:
        return "Python is cool"
    else:
        text = text.replace('-', " ")
        return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ returs whether n is a number """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
