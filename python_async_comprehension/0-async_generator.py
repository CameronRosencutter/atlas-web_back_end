#!/usr/bin/env python3

"""This will loop 10 times, then choose a number from 1-10 at random"""
import asyncio
import random


async def async_generator():
    """loops several times, then chooses a number 1-10 at random"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
