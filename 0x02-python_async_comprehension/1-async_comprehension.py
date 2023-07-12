#!/usr/bin/env python3

""" Async Comprehensions """

import asyncio
import random
from 0-async_generator.py import async_generator

async def async_comprehension():
    random_numbers = [number async for number in async_generator()]
    return random_numbers
