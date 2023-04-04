#!/usr/bin/env python3
"""
A coroutine that takes no args
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Loop ten times async and wait one sec then
    give a random number. """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
