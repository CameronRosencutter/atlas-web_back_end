#!/usr/bin/env python3
"""
This is the db.py file
"""


from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker, Session

# Existing imports...

class DB:
    # Existing code...

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

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
