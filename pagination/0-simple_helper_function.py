#!/usr/bin/env python3
"""Behold, a very simple function!"""


def index_range(page, page_size):
    """Start, end, tuple, size, index, it has everyhting!!"""
    start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return (start_index, end_index)
