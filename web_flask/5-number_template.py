#!/usr/bin/python3
""" The simple web application that start a websrver
    based on flask framework
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ return hello HBNB text """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB text """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ Return custom text """
    return f"C {text}"


@app.route('/python', defaults={"text": "is cool"})
@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Return custom text """
    if len(text) == 0:
        return "Python is cool"
    else:
        text = text.replace('-', " ")
        return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ return whether n is a number """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """ render response in template """
    params = {
        "n": n
    }
    return render_template('5-number.html', **params)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
