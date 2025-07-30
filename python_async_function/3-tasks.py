#!/usr/bin/env python3
"""inport la fonction wait_ramdom"""


import asyncio
wait_random = __import__ ('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> asyncio.tasks:
    """execute la fonction wait_random"""
    return asyncio.create_task(wait_random(max_delay))
