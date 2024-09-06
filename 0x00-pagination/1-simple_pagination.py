#!/usr/bin/env python3

import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range

"""
1. Simple pagination
"""


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        if page == 0 or page_size == 0:
            assert page != 0
            assert page_size != 0

        if page < 0 or page_size < 0:
            assert page < 0
            assert page_size < 0

        page_index = index_range(page, page_size)

        mydataset = self.dataset()

        data = []

        try:
            data = mydataset[page_index[0]:page_index[1]]
        except IndexError:
            return []

        return data
