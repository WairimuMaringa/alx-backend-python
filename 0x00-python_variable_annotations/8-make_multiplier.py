#!/usr/bin/env python3
"""
type annotated function makemultiplier that takes a float
multiplier as argument and returns a function that multiplies
a float by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return function. """
    def multiplier_fn(number: float) -> float:
        """ multiply float and the multiplier. """
        return number * multiplier

    return multiplier_fn
