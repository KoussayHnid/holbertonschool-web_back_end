#!/usr/bin/env python3
"""
This module defines a function for calculating index ranges for pagination.
"""


def index_range(page, page_size):
    """
    Return a tuple of start and end indexes for a given page and page size
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
