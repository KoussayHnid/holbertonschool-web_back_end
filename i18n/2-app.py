#!/usr/bin/env python3
"""basic Flask app"""
from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)

SUPPORTED_LANGUAGES = ['en', 'es', 'fr', 'de']

babel = Babel()

def get_locale():
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)

babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
