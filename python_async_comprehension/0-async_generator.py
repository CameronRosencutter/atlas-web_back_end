#!/usr/bin/env python3
'''please please please work'''

import asyncio
import random


async def async_generator():
    """I dont know what is wrong anytmore"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)


# Example usage
async def main():
    """Am i eternally curesed? Why why why!!"""
    async for number in async_generator():
        print(number)


# Run the event loop
asyncio.run(main())
