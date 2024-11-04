#!/usr/bin/env python3
"""basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

SUPPORTED_LANGUAGES = ['en', 'fr']

babel = Babel(app)


def get_locale():
    locale = request.args.get('locale')
    if locale in SUPPORTED_LANGUAGES:
        return locale
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home():
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
