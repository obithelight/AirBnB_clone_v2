#!/usr/bin/python3
'''A Python Module'''


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''displays hello hbnb'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''displays hbnb'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''displays c plus a variable text'''
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
