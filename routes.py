__author__ = 'Keshan'

# all the imports

from flask import Flask, render_template, request, abort
import requests

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run(debug=True)