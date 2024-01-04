#!/usr/bin/env python3
'''info'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''return to tuple'''
    return k, float(v ** 2)
