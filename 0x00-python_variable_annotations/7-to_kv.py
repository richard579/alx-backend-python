#!/usr/bin/env python3
"""type-annotated function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns Tuple of a string and a float"""
    x = v ** 2
    return (k, x)
