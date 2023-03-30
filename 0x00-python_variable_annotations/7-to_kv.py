#!/usr/bin/env python3
"""
type annotated function tokv that takes string k and an int or
float v as arguments and returns a tuple
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Return tuple. """
    return (k, v**2)
