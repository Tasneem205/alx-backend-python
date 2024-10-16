#!/usr/bin/env python3
"""
task 0
"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """generator to generate rand numbers every second"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
