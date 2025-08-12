#!/usr/bin/env python3
"""import measure_runtime function."""

from typing import Final
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return"""
    start: Final[float] = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: Final[float] = time.perf_counter()
    return end - start
