#!/usr/bin/env python3
def index_range(page, page_size):
    """
    Return a tuple of start and end indexes for a given page and page size
    """
    """Returns:
        tuple: A tuple containing the start and end indexes (0-indexed) for the given page.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
