#!/usr/bin/env python3
"""
1. Basic Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel
import pytz


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configs for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config['LANGUAGES'] = Config.LANGUAGES
app.config['BABEL_DEFAULT_LOCALE'] = Config.BABEL_DEFAULT_LOCALE
app.config['BABEL_DEFAULT_TIMEZONE'] = Config.BABEL_DEFAULT_TIMEZONE


@app.route('/')
def index():
    """Home Page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
