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
        """
        init function
        """
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
        """
        My get page function
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        if page == 0 or page_size == 0:
            assert page != 0
            assert page_size != 0

        if page < 1 or page_size < 1:
            assert page < 1
            assert page_size < 1

        page_index = index_range(page, page_size)

        mydataset = self.dataset()

        data = []

        try:
            data = mydataset[page_index[0]:page_index[1]]
        except IndexError:
            return []

        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Get hyper data from the list with extra info
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())  # Total items in the dataset
        total_pages = math.ceil(total_items / page_size)  # Calcula

        if page <= 1:
            prev_page = None
        else:
            prev_page = page - 1

        if page >= total_pages:
            next_page = None
        else:
            next_page = page + 1

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
