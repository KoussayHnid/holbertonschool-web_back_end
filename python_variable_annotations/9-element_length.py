#!/usr/bin/env python3
"""function that return values with the appropriate types"""
from typing import List, Tuple, Sequence


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements in a list and return a list of tuples.
    """
    return [(i, len(i)) for i in lst]
