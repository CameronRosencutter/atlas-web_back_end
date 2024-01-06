#!/usr/bin/env python3
"""find 10 numbers."""


from typing import List


async_ = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """10 random numbers."""
    aleatorio = [i async for i in async_()]
    return aleatorio
