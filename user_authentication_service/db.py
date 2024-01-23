#!/usr/bin/env python3
"""
This is the db.py file
"""

from sqlalchemy.exc import IntegrityError  # Import this for handling potential integrity errors

# Existing imports...

class DB:
    # Existing code...

    def add_user(self, email: str, hashed_password: str):
        """Add a new user to the database.

        Args:
            email (str): User's email address.
            hashed_password (str): Hashed password for the user.

        Returns:
            User: The created User object.
        """
        from user import User  # Import the User class

        # Create a new User instance
        new_user = User(email=email, hashed_password=hashed_password)

        # Add the user to the session
        self._session.add(new_user)

        try:
            # Commit the changes to the database
            self._session.commit()
        except IntegrityError as e:
            # Handle integrity errors, for example, if the email is not unique
            self._session.rollback()
            raise ValueError("User with this email already exists.") from e

        return new_user
