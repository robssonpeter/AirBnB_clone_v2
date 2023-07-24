#!/usr/bin/python3
""" The simple web application that start a websrver
    based on flask framework
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns the HBNB Text """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns the HBNB Text """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
