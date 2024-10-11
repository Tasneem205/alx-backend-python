#!/usr/bin/env python3
"""mixed list typing"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """to sum ints and floats"""
    return sum(mxd_lst)
