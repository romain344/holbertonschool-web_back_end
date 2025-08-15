#!/usr/bin/env python3
"""définie la classe Server"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server clas"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """donnees du dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """donnees indexées"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """retourne à le dictionnaire contenant les données paginées`"""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        max_index = max(indexed_data.keys()) if indexed_data else -1

        assert index <= max_index

        data = []
        current_index = index

        while len(data) < page_size and current_index <= max_index:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index if current_index <= max_index else None

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
