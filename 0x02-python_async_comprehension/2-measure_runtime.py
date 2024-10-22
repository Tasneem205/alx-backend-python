#!/usr/bin/env python3
"""
task 2
"""
import asyncio
import time
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the run time of 4 asynccomperhention"""
    start_time = time.perf_counter()
    tasks: List = [
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    ]
    await gather(*tasks)
    end_time = time.perf_counter()  # Record the end time
    return end_time - start_time
