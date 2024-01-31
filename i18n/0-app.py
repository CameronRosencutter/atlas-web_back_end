#!/usr/bin/env python3
"""This is the 0app file in use"""

# File: i18n/0-app.py
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Instantiate Babel and store it in a module-level variable
babel = Babel(app)

# Config class for Flask app
class Config:
    # Available languages for the app
    LANGUAGES = ["en", "fr"]
    # Default locale and timezone settings
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)  # Use Config as config for the Flask app

# Define a route
@app.route('/')
def index():
    return render_template('0-index.html')

# ... (Rest of your existing code)

if __name__ == '__main__':
    app.run(debug=True)
