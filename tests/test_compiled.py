from __future__ import annotations

from ctypes.util import find_library

import pylibmagic


def test_find_library():
    lib_path = find_library("magic")
    assert lib_path is not None
    assert lib_path.startswith(str(pylibmagic.data))


def test_run_magic():
    import magic

    result = magic.from_file(pylibmagic.data / "__init__.py")
    assert result
    assert result == "Python script, ASCII text executable"
