#!/usr/bin/env python3
"""
Annotate the given function
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return the length of elements. """
    return [(i, len(i)) for i in lst]
