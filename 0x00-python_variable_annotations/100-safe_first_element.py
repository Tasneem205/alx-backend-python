#!/usr/bin/env python3
"""task 101"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """return the first elemnet in a list"""
    if lst:
        return lst[0]
    else:
        return None
