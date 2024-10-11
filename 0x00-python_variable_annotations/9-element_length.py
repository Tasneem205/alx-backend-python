#!/usr/bin/env python3
"""annotate this function task"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """the function after annotation"""
    return [(i, len(i)) for i in lst]
