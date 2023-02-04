#!/usr/bin/python3
"""Your web application must be listening on 0.0.0.0, port 5000
Routes:

    /: display 'Hello HBNB!'
    /hbnb: display 'HBNB'
    /c/<text>: display 'C', followed by the value of the text variable
    /python/(<text>): display 'Python'  + value of the text variable
        The default value of text is is cool
    /number/<n>: display n is a number  only if n is an integer
"""
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
def python_route(text="is cool"):
    """Displays Python followed by route"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>')
def number_route(n):
    """Displays n is a number"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
