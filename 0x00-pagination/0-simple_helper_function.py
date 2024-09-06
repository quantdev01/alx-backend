#!/usr/bin/env python3

"""
Return the range index
"""


def index_range(page, page_size):
    """
    Function to return range to print based on page we are on
    and the page size
    """
    last_index = page_size * page
    first_index = last_index - page_size

    return (first_index, last_index)
