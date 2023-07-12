#!/usr/bin/env python3
import asyncio
import random

async_generator = __import__('0-async_generator').async_generator

async def async_generator():
    """coroutine called async_generator that takes no arguments.
        Arguments : None
        Return: yielded random numbers range(0,10)
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
asyncio.run(async_generator())

