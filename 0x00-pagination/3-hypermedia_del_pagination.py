#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """Last hyper
        """
        indexed_data = self.indexed_dataset()

        # Determine the range of data to return
        data = []
        next_index = None

        for i in range(index, index + page_size):
            if i in indexed_data:
                data.append(indexed_data[i])
            else:
                # Break loop if we encounter an index not in the dataset
                break

        # Calculate the next index
        next_index = index + page_size if len(data) == page_size else None

        return {
            'page_size': len(data),
            'data': data,
            'next_index': next_index
        }
