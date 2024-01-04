#!/usr/bin/env python3
'''return sum as float'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """find the sum of the arguments"""
    return sum(mxd_lst)
