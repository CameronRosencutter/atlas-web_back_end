#!/usr/bin/env python3
"""This will fiilter out information"""

import re


def filter_datum(fields, redaction, message, separator):
    return re.sub(fr'(?<=\{separator}|^)({"|".join(fields)})\{separator}', f'{redaction}{separator}', message)
