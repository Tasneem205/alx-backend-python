#!/usr/bin/env python3
"""task 8 function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function to run other function"""
    def multiply(value: float) -> float:
        """function to multiply"""
        return multiplier * value
    return multiply
