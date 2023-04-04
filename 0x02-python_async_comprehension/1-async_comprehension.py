#!/usr/bin/env python3
"""
Import from task zero and write a coroutine
that takes no args
"""
import random
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collect ten random numbers then return them
    while using async comprehensing. """
    outcome = [i async for i in async_generator()]
    return outcome
