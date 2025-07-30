#!/usr/bin/env python3
"""execute la fonction"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Génère 10 valeurs aléatoires entre 0 et 10 avec un délai d'1 seconde entre chaque"""
for _ in range(10):
    await asyncio.sleep(1)
    yield random.uniform(0, 10)
