#!/usr/bin/env python3
'''a type annotated function'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculate the sums"""
    return sum(input_list)
