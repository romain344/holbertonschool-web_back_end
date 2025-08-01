#!/usr/bin/env python3
"""défine la fonction"""


import asyncio
import random


async def async_generator():
    """génère des nombres aléatoires"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
