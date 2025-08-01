
#!/usr/bin/env python3
"""Async comprehension that collects random numbers"""

from typing import List
from importlib import import_module

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers from an async generator"""
    return [i async for i in async_generator()]
