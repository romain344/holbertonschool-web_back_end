#!/usr/bin/env python3
"""Définit la coroutine async wait_random"""


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Exécute wait_random"""
    delays: List[float] = []

    async def get_and_store_delay():
        delay = await wait_random(max_delay)
        delays.append(delay)

    tasks = [asyncio.create_task(get_and_store_delay()) for _ in range(n)]
    await asyncio.gather(*tasks)

    sorted_delays: List[float] = []
    for d in delays:
        for i in range(len(sorted_delays)):
            if d < sorted_delays[i]:
                sorted_delays.insert(i, d)
                break
        else:
            sorted_delays.append(d)

    return sorted_delays
