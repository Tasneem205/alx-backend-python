#!/usr/bin/env python3
"""wait n times function file"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """wait random amout of time for n times"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    arr = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        arr.append(delay)

    return arr
