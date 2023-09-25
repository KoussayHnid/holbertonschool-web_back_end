#!/usr/bin/env python3
"""function that return values with appropriate types"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Calculate the length of elements in a list and return a list of tuples.
    """
    return [(i, len(i)) for i in lst]
