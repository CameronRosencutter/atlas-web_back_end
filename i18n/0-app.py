#!/usr/bin/env python3
"""This is the 0app file in use"""

# File: i18n/0-app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """This is the function index"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
