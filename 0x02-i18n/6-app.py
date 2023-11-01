#!/usr/bin/env python3
"""
 6. Use user locale
"""
from flask import g
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configs for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Determine the best match from supported languages"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> int:
    """Retrieves a user based on a user id.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id), None)


@app.before_request
def before_request():
    """Use get_user to find a user, set it as global object"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    """Home Page"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
