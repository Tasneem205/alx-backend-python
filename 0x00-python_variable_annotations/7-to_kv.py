#!/usr/bin/env python3
"""task 7 to kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to kv function"""
    return (k, v ** 2)
