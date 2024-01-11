#!/usr/bin/env python3
"""Behold, a very simple function!"""

import csv


def index_range(page, page_size):
    """this is the index range for page and pagesize"""
    # Calculate the start index for the given page and page size
    start_index = (page - 1) * page_size

    # Calculate the end index for the given page and page size
    end_index = start_index + page_size

    # Return a tuple containing the start and end indexes
    return start_index, end_index


def get_page(page: int = 1, page_size: int = 10):
    """This is used to find page amount"""
    # Check if page and page_size are integers greater than 0
    assert isinstance(page, int) and page > 0
    "Page must be an integer greater than 0"
    assert isinstance(page_size, int) and page_size > 0
    "Page size must be an integer greater than 0"

    with open('your_csv_file.csv', 'r') as file:
        reader = csv.reader(file)
        dataset = list(reader)

    # Use index_range to find the correct indexes for pagination
    start_index, end_index = index_range(page, page_size)

    # Check if the indexes are within the range of the dataset
    if start_index >= len(dataset) or end_index <= 0:
        return []  # Return an empty list if out of range

    # Return the appropriate page of the dataset
    return dataset[start_index:end_index]
