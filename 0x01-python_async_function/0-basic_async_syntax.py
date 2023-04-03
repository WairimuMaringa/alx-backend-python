#!/usr/bin/python3
"""
Asnyc function that takes an argument that waits for a
random delay between 0 and the arg seconds and returns it
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for delay and returns the argument. """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
