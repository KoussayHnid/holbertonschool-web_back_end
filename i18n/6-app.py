#!/usr/bin/env python3
"""basic Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Define supported languages
SUPPORTED_LANGUAGES = ['en', 'fr']

# Initialize Babel
babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_locale():
    # 1. Check if 'locale' is in the URL parameters
    locale = request.args.get('locale')
    if locale in SUPPORTED_LANGUAGES:
        return locale

    # 2. Check user's preferred locale if the user is logged in
    if g.user and g.user.get("locale") in SUPPORTED_LANGUAGES:
        return g.user["locale"]

    # 3. Fall back to the best match from the request headers
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)


# Initialize Babel with the locale selector function
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home():
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
