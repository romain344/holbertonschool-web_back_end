#!/usr/bin/env python3
"""Définit la fonction sum_mixed_list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Renvoie la somme des éléments d'une liste mixte"""
    return float(sum(mxd_lst))
