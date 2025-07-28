#!/usr/bin/python3
"""Définit la fonction make_multiplier"""


from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Retourne une fonction qui multiplie une valeur par multiplier"""
    
    def multiplier_function(value: float) -> float:
        return value * multiplier
    
    return multiplier_function
