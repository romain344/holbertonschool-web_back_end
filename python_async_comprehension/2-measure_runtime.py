#!/usr/bin/env python3
"""import asyncio and time to measure runtime"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return the total runtime of four parallel comprehensions"""
    start_time = time.perf_counter()
    
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = time.perf_counter()
    return end_time - start_time
