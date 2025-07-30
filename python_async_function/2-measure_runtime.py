#!/usr/bin/python3
"""Définit la coroutine async wait_n"""


import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n, max_delay) -> float:
    """calcule le temps moiyent pour executer une fonction"""
    start = time.perf_counter()
    await wait_n(n, max_delay)
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
