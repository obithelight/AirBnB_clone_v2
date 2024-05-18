#!/usr/bin/python3
'''A Python Module'''


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''displays Hello HBNB!'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''displays HBNB'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''displays C plus a variable string'''
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    '''displays Python plus a variable string'''
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''displays n is a number if n is an integer'''
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''displays a HTML page if n is an integer'''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    '''displays a HTML page if n is an integer'''
    even_odd = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', number=n,
                           even_odd=even_odd)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
