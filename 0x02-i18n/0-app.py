#!/usr/bin/env python3
"""
 0. Basic Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app=app)


@app.route('/')
def index():
    title = _('Welcome to Holberton')
    header = _('Hello world')
    """Home Page"""
    return render_template('0-index.html', home_title=title,
                           home_header=header)


if __name__ == '__main__':
    app.run(debug=True)
