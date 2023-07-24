""" The simple web application that start a websrver
    based on flask framework
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Returns hello HBNB text """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB text """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    return f"C {text}"


@app.route('/python', defaults={"text": "is cool"})
@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ returns custom text """
    if len(text) == 0:
        return "Python is cool"
    else:
        text = text.replace('-', " ")
        return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ returs whether n is a number """
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def template(n):
    """ renders a number in a template """
    params = {
        "n": n
    }
    return render_template('5-number.html', **params)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ returns whether a number is even or odd """
    if n % 2:
        type = "odd"
    else:
        type = "even"
    params = {
        "n": n,
        "type": type
    }
    return render_template('6-number_odd_or_even.html', **params)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
