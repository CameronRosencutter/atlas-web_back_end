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


def get_hyper(page: int = 1, page_size: int = 10):
    """This is the gt hyper function"""
    assert isinstance(page, int) and page > 0
    "Page must be an integer greater than 0"
    assert isinstance(page_size, int) and page_size > 0
    "Page size must be an integer greater than 0"

    dataset_page = get_page(page, page_size)
    total_pages = math.ceil(len(dataset_page) / page_size)

    next_page = page + 1 if page * page_size < len(dataset_page) else None
    prev_page = page - 1 if page > 1 else None

    return {
        'page_size': len(dataset_page),
        'page': page,
        'data': dataset_page,
        'next_page': next_page,
        'prev_page': prev_page,
        'total_pages': total_pages
    }
