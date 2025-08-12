#!/usr/bin/env python3
"""execute la fonction index_page"""


def index_page(page, page_size):
    """retorune à start en end pour la page de données"""
    start =  (page - 1) * page_size
    end = start * page_size
    return (start, end)
