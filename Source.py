__author__ = 'Keshan'

# all the imports

from flask import Flask , render_template, request, abort
import requests
from contextlib import closing


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'




@app.route('/hello/')

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug = True)
