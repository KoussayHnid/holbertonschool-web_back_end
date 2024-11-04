#!/usr/bin/env python3
"""basic Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

SUPPORTED_LANGUAGES = ['en', 'fr']

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale():
    locale = request.args.get('locale')
    if locale in SUPPORTED_LANGUAGES:
        return locale
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)


babel.init_app(app, locale_selector=get_locale)


def get_user():
    """Retrieve a user based on the login_as URL parameter."""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Set g.user to the logged-in user, if any."""
    g.user = get_user()


@app.route('/')
def home():
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
