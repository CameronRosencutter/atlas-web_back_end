#!/usr/bin/env python3

"""For protection of passwords and security"""


import bcrypt


def hash_password(password: str) -> bytes:
    """Make a password hashed and protected"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
