#!/usr/bin/env python3
import asyncio
from 0-basic_async_syntax.py import wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    An async routine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random.

    Returns:
        list[float]: The list of delays (float values) in ascending order.

    """
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
    prior_result = await delay
        all_delays.append(prior_result)
    return all_delays

