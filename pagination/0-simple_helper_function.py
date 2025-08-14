#!/usr/bin/env python3
"""execute la fonction index_page"""

from typing import Tuple


def index_page(page: int, page_size: int) -> Tuple[int, int]:
    """retourne à start en end pour la page de données"""
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return start_index, end_index
