#!/usr/bin/env python3
"""execute la fonction index_page"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """retourne à start en end pour la page de données"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
