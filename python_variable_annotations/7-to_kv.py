#!/usr/bin/env python3
"""Définit la fonction to_kv"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Retourne un tuple (k, v²) où v² est un float"""
    return (k, float(v ** 2))
