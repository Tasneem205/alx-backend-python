#!/usr/bin/env python3
"""task 101"""
from typing import TypeVar, Any, Union, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """return value of a key in dict"""
    if key in dct:
        return dct[key]
    else:
        return default
