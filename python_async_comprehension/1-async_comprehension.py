#!/usr/bin/env python3
"""Async Comprehensions module"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """génere 10 nobre"""
    return [i async for i in async_generator()]
