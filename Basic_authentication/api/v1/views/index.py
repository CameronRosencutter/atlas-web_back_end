#!/usr/bin/env python3
"""This is the index.py"""

from flask import Blueprint, abort

index = Blueprint('index', __name__)

# Existing routes...

@index.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized_endpoint():
    """IF its unauthorized, it aborts as a 401"""
    # Raise a 401 error using abort
    abort(401)


@bp.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    # Raise a 401 error using abort
    abort(401)
    