#!/usr/bin/env python3
"""
1. Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configs for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
# app.config['LANGUAGES'] = Config.LANGUAGES
# app.config['BABEL_DEFAULT_LOCALE'] = Config.BABEL_DEFAULT_LOCALE
# app.config['BABEL_DEFAULT_TIMEZONE'] = Config.BABEL_DEFAULT_TIMEZONE


@app.route('/')
def index():
    """Home Page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
