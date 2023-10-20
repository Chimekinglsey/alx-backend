#!/usr/bin/env python3
"""
0 - simple helper function.py
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tuples matching the range of indexes """
    if page <= 0:
        new_page = 0
        return(new_page, page_size)
    else:
        new_page = page - 1
        return(new_page * page_size, page_size * page)
