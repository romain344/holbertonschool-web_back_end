#!/usr/bin/env python3
"""Fonction qui retourne une tâche asyncio à partir de wait_random"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Crée une tâche asyncio à partir de wait_random"""
    return asyncio.create_task(wait_random(max_delay))
