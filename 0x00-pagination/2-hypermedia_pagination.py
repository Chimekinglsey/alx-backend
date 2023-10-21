#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple matching the range of indexes
    """
    if page <= 0:
        new_page = 0
        return (new_page, page_size)
    else:
        new_page = page - 1
        return (new_page * page_size, (new_page * page_size) + page_size)


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
        """ Retrieves items based on pages """
        assert isinstance(page, int) and page > 0
        assert type(page_size) == int and page_size > 0

        file_size = len(self.dataset())
        result = index_range(page, page_size)
        start_index, stop_index = result

        if start_index >= file_size:
            return []
        return self.dataset()[start_index:stop_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ returns a dictionary of get_page() with navigation"""
        result = self.get_page(page, page_size)
        max_page, max_page_size = index_range(page, page_size)
        total_max_page = len(self.dataset())
        total_pages = math.ceil((total_max_page)/page_size)
        next_p = page + 1 if page_size <= max_page and page - 1 > 0 else None
        prev_page = page - 1 if page > 1 else None
        if max_page_size > total_max_page:
            page_size = 0
            next_p = None

        return {
                'page_size': page_size, 'page': page,
                'data': result, 'next_page': next_p,
                'prev_page': prev_page, 'total_pages': total_pages
                }
