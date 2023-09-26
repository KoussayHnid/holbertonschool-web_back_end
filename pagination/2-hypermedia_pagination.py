#!/usr/bin/env python3
"""function that take the same arguments and return a dictionary"""
import math
import csv
from typing import List


class Server:
    def index_range(self, page, page_size):
        """
        Return a tuple of start and end indexes for a given page and page size
        """
        if page <= 0 or page_size <= 0:
            raise ValueError("Page and page_size must be positive integers.")

        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return start_index, end_index

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
        Retrieves a specific page of data from the dataset
        """
        if not isinstance(
                page,
                int) or not isinstance(
                page_size,
                int) or page <= 0 or page_size <= 0:
            raise AssertionError(
                "AssertionError raised with negative values or non-integers")

        start_index, end_index = self.index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """
        Retrieves a dictionary with hyper-paging information.
        """
        if not isinstance(
                page,
                int) or not isinstance(
                page_size,
                int) or page <= 0 or page_size <= 0:
            raise AssertionError(
                "AssertionError raised with negative values or non-integers")

        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        start_index, end_index = self.index_range(page, page_size)

        if start_index >= len(dataset):
            return {
                'page_size': 0,
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': None,
                'total_pages': total_pages
            }

        current_page_data = self.get_page(page, page_size)
        next_page = page + 1 if end_index < len(dataset) else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(current_page_data),
            'page': page,
            'data': current_page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
