#!/usr/bin/env python3
"""
Type annotated list summixedlist that takes a list of integers
and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """ Returns sum of a mixed list. """
    return sum(input_list)
