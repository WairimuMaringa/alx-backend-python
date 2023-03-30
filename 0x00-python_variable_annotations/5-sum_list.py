#!/usr/bin/env python3
"""
Type annotated function sumlist that takes a list of floats
and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Return sum of lists. """
    return sum(input_list)
