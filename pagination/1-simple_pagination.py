#!/usr/bin/env python3
"""function simple_pagination"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Return a tuple of start and end indexes for a given page and page size
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """ The `Server` class is designed
    for paginating a dataset from a CSV file"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Retrieves and caches the dataset from
          the CSV data file, excluding the header row.
"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset"""

        if not isinstance(
                page,
                int) or not isinstance(
                page_size,
                int) or page <= 0 or page_size <= 0:
            raise AssertionError(
                "AssertionError raised with negative values or non-integers")

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
