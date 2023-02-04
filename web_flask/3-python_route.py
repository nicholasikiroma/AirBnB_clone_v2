#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Displays welcome message"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_hbnb():
    """Displays strict with specified route"""
    return "HBNB"


@app.route('/c/<text>')
def hello_c(text):
    """Display 'C' to the screen"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python')
@app.route('/python/<text>')
def python_route(text):
    """Displays Python followed by route"""
    text = text.replace("_", " ")
    return "Python %s" % text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
