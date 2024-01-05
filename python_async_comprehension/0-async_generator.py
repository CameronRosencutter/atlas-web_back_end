#!/usr/bin/env python3
'''take no arguments'''

import asyncio
import random


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


# Example of using the async_generator coroutine
async def main():
    async for number in async_generator():
        print(number)
