#!/usr/bin/python3
"""Définit la coroutine async wait_n"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """calcule le temps moiyent pour executer une fonction"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    sorted_delays: List[float] = []
    for delay in results:
        inserted = False
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)

    return sorted_delays