#!/usr/bin/env python3
'''wtire a annotated function'''


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """return appropriate types"""
    return [(i, len(i)) for i in lst]
