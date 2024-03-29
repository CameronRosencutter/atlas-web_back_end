#!/usr/bin/env python3
"""This will fiilter out information"""

import re
from typing import List
import logging
import os
import mysql.connector
import datetime

PII_FIELDS = ('phone', 'password', 'email', 'ssn', 'name')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """This is the init function that works"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """This is used to format the proper info needed"""
        log_message = super().format(record)
        result = filter_datum(self.fields, self.REDACTION,
                              log_message, self.SEPARATOR)
        return result

def main():
    """Retrieve all rows in the users table and
    display each row in a filtered format."""
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()

    # Retrieve all rows in the users table
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()

    # Display each row in a filtered format
    for row in rows:
        filtered_row = filter_datum(
            PII_FIELDS, RedactingFormatter.REDACTION, str(row), ";"
            )
        logger.info(
            "[HOLBERTON] user_data INFO %s: %s;",
            str(datetime.datetime.now()), filtered_row
            )

    # Display filtered fields
    logger.info("Filtered fields:\n%s", "\n".join(PII_FIELDS))

    cursor.close()
    db.close()


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """I really hope this"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to the MySQL database using environment variables."""
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')

    # Create a connection to the MySQL database
    db = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )

    return db


if __name__ == "__main__":
    main()