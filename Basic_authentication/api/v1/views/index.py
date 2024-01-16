#!/usr/bin/env python3
"""This is the index.py"""

from flask import Blueprint, abort

index = Blueprint('index', __name__)

# Existing routes...

@index.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized_endpoint():
    # Raise a 401 error using abort
    abort(401)
