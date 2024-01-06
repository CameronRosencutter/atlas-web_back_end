#!/usr/bin/env python3
"""please please work for me"""


import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """you wanna work. i know you do"""
    inicio = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    fin = asyncio.get_event_loop().time()
    return fin - inicio
