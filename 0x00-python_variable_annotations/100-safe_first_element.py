#!/usr/bin/env python3
"""
Augment the given code
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return list or none. """
    if lst:
        return lst[0]
    else:
        return None
