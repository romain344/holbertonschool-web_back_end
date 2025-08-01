#!/usr/bin/env python3
"""import pour le code"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """genere les nonbre"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
