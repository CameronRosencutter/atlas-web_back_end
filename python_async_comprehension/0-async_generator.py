#!/usr/bin/env python3
'''words'''

import asyncio
import random

async def async_generator():
    """morewords"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)


# Example usage
async def main():
    """moremorewords"""
    async for number in async_generator():
        print(number)


# Run the event loop
asyncio.run(main())