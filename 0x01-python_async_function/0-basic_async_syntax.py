#!/usr/bin/env python3
"""wait random delay function file"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """wait random amount of time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
