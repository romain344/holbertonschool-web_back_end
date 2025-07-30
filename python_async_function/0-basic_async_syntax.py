#!/usr/bin/env python3
"""défine la fonction async wait_random"""


import random
import asyncio


async def wait_random(max_delay):
    """choissi un temps dattante entre 0 et 10"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
