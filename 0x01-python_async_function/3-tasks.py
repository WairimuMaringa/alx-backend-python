#!/usr/bin/env python3
"""
Import from task zero and write a regular nonasync function
that takes an integer and returns a asyncio task
"""
from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Return asyncio task. """
    task = create_task(wait_random(max_delay))
    return task
