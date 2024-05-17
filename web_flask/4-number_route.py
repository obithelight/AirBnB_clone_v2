#!/usr/bin/python3
'''A Python Module'''


from flask import Flask
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
    '''displays c plus a variable text'''
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    '''displays python plus a variable text'''
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Flask ensures that n is an integer because of <int:n>'''
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
