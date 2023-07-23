""" The simple web application that start a websrver
    based on flask framework
"""

from flask import Flask, render_template

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

@app.route('/python', defaults={"text":"is cool"})
@app.route('/python/', defaults={"text":"is cool"})
@app.route('/python/<text>')
def python(text):
    if len(text) == 0:
        return "Python is cool"
    else:
        text = text.replace('-', " ")
        return f"Python {text}"

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"

@app.route('/number_template/<int:n>')
def template(n):
    params = {
        "n": n
    }
    return render_template('5-number.html', **params)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
