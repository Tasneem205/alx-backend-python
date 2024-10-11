#!/usr/bin/env python3
"""annotate this function task"""
from typing import List, Tuple, Any


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """the function after annotation"""
    return [(i, len(i)) for i in lst]

