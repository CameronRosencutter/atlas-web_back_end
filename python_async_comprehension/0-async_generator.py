#!/usr/bin/env python3

"""jiljil"""
import asyncio
import random


async def async_generator():
    """10 random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def main():
    # Create an event loop
    loop = asyncio.get_event_loop()

    # Run the async_generator and print each result
    async for result in async_generator():
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
    