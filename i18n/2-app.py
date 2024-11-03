#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)

# Configure supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LANGUAGES'] = ['en', 'es', 'fr']

# Initialize Babel
babel = Babel(app)

# Custom get_locale function to determine the best match for the user's language preference
@babel.localeselector
def get_locale():
    # Using request.accept_languages to find the best match for supported languages
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LANGUAGES'])

# Route for index page
@app.route('/')
def index():
    return render_template('2-index.html')

if __name__ == "__main__":
    app.run(debug=True)
