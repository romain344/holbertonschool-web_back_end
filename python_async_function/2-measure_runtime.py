#!/usr/bin/python3
"""Définit la coroutine async wait_n"""

import asyncio
from typing import List
from concurrent_coroutines import wait_random
async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        delays.append(result)

    return delays
