#!/usr/bin/env python3
"""Définit la coroutine async wait_random"""

import random
import asyncio

async def wait_random(max_delay=10):
    """retourne à delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
