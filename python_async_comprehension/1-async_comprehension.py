#!/usr/bin/env python3
"""definit la fonction"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collecte 10 valeurs depuis async_generator et les retourne dans une liste."""
    return [value async for value in async_generator()]
