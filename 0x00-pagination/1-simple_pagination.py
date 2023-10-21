#!/usr/bin/env python3
"""
1 - simple_pagination.py
"""
from typing import Tuple
import csv
from typing import List


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tuples matching the range of indexes """
    if page <= 0:
        new_page = 0
        return(new_page, page_size)
    else:
        new_page = page - 1
        return(new_page * page_size, page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """retrieves items based on pages"""
        file_size = len(self.dataset())
        file = self.dataset()
        assert page > 0 and type(page) == int
        assert type(page_size) == int
        # assert page_size > 0

        result = index_range(page, page_size)
        start_index = result[0]
        stop_index = result[1]

        count, return_list = 0, []
        if start_index <= file_size and stop_index <= file_size:
            while count < stop_index:
                if start_index < file_size:
                    return_list.append(file[start_index])
                    start_index += 1

                count += 1
        return return_list

#         pass
# data = Server()
# print(data.get_page(6, 4))
