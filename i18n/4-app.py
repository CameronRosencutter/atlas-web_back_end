#!/usr/bin/env python3
"""This is the 0app file in use"""

from flask import Flask, request, g
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)

# Configure the supported locales
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

# Mock translations for demonstration purposes
translations = {
    'en': {'hello_world': 'Hello World!'},
    'fr': {'hello_world': 'Bonjour Monde!'}
}


@babel.localeselector
def get_locale():
    # Check if the locale parameter is present in the request URL
    locale = request.args.get('locale')

    # If the locale is supported, return it
    if locale and locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale

    # If not, resort to the default behavior
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])


@app.route('/')
def index():
    # Get the translated text based on the current locale
    hello_world_translation = _(translations.get(str(g.get('locale', '')), {}).get('hello_world', 'Hello World!'))

    # Display the translated text
    return f"<h1>{hello_world_translation}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
