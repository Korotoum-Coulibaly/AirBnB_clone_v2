#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """ Function that  display hello on computer screen"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ Function that display hbnb on computer screen"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_by_value_text(text):
    """ Function that returns C with the text"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_is_fun(text="is_cool"):
    """ Function that returns python on a womputer screen"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Function that returns number on a computer screen"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Function that return number in template"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Function that return number odd or even"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', number=n,
                               pair="even")
    else:
        return render_template('6-number_odd_or_even.html', number=n,
                               pair="odd")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
