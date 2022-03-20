from __future__ import annotations

from ctypes.util import find_library


def test_find_library():
    assert find_library("magic") is not None
