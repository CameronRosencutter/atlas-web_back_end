#!/usr/bin/env python3
"""this is the auth.py file
"""

import bcrypt

def _hash_password(password: str) -> bytes:
    """This will be the hash password part"""
    # Generate a random salt
    salt = bcrypt.gensalt()
    
    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # Return the hashed password as bytes
    return hashed_password
