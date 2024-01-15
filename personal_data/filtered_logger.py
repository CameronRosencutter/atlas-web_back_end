#!/usr/bin/env python3
"""This will fiilter out information"""

import re


def filter_datum(fields, redaction, message, separator):
    pattern = fr'({separator.join(fields)})=[^{separator}]+'
    return re.sub(pattern, f'\\1={redaction}', message)
