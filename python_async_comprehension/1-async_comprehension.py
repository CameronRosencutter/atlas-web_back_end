#!/usr/bin/env python3
"""will collect 10 random numbers using an
async comprehensing over async_generator"""
import asyncio
from typing import List
async_ = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return the 10 random numbers."""
    aleatorio = [i async for i in async_()]
    return aleatorio
