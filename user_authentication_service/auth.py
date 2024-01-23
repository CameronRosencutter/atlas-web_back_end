#!/usr/bin/env python3
"""this is the auth.py file
"""

from db import DB
from user import User  # Assuming you have a User class defined
import bcrypt

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str):
        # ... (previous implementation)

    def valid_login(self, email: str, password: str) -> bool:
        # Locate the user by email
        user = self._db.get_user_by_email(email)

        # Check if the user exists and the password matches
        if user and bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
            return True

        return False

    @staticmethod
    def _hash_password(password: str) -> bytes:
        # Hash the password using bcrypt
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Assuming you have a User class defined with an appropriate __init__ method
