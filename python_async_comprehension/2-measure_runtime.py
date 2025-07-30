#!/usr/bin/env python3
"""Mesure le temps d'exécution pour 4 async_comprehension exécutées en parallèle."""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Mesure le temps pour exécuter 4 fois async_comprehension en parallèle."""
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
