#!/usr/bin/env python3
"""
1. Basic Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel
import pytz


app = Flask(__name__)
# app.config['LANGUAGES'] = ["en", "fr"]
# app.config['BABEL_DEFAULT_LOCALE'] = 'en'
# app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


babel = Babel(app, config=Config)


@app.route('/')
def index():
    """Home Page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)