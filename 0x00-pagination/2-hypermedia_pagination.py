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
        Load and cache the dataset from a CSV file.

        Returns:
            List[List]: The dataset excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of the dataset.

        Args:
            page (int): The page number to retrieve (1-based index). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: The page of data corresponding to the requested page.

        Raises:
            ValueError: If `page` or `page_size` is less than 1.
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
        Retrieve a page of the dataset with additional pagination information.

        Args:
            page (int): The page number to retrieve (1-based index). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing the following key-value pairs:
                - 'page_size': The length of the returned dataset page.
                - 'page': The current page number.
                - 'data': The dataset page (equivalent to the return value from get_page).
                - 'next_page': The number of the next page, or None if no next page.
                - 'prev_page': The number of the previous page, or None if no previous page.
                - 'total_pages': The total number of pages in the dataset.
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
