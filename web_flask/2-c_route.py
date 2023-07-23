""" The simple web application that start a websrver
    based on flask framework
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def text(text):
    return f"C {text}"

if __name__ == "__main__":
    app.run()
