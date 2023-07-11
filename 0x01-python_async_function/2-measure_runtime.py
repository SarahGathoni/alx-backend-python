#!/usr/bin/env python3
from wait_random import 0-basic_async_syntax
"""a function that uses a regular function syntax
    that takes an integer max_delay and returns a asyncio.Task"""
import asyncio
import time
task_wait_random = __import__('3-tasks').task_wait_random


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
