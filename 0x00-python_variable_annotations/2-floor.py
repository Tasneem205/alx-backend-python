#!/usr/bin/env python3
"""type-annotated function floor"""


def floor(n: float) -> int:
    """to use math module"""
    if n >= 0:
        return int(n)
    else:
        return int(n) - 1 if n != int(n) else int(n)
