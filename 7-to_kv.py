#!/usr/bin/python3
"""définie la fonction to_kv"""


def to_kv(k: str, v: (int | float)) -> tuple[str, float]:
	"""retourne un tuple contenant la clé et le carré de la valeur"""
	return (k, float(v ** 2))
