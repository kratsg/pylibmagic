from __future__ import annotations

import importlib
from ctypes.util import find_library

import pytest

import pylibmagic


def test_run_magic():
    import magic

    result = magic.from_file(pylibmagic.data / "__init__.py")
    assert result
    assert result == "Python script, ASCII text executable"


def test_run_magic_fail(monkeypatch):
    import magic

    monkeypatch.delenv("MAGIC", raising=True)
    result = magic.from_file(pylibmagic.data / "__init__.py")
    assert result
    assert result == "Python script, ASCII text executable"


def test_find_library():
    lib_path = find_library("magic")
    assert lib_path is not None


def test_import_magic_fail(monkeypatch):
    import magic

    for key in pylibmagic.keys:
        monkeypatch.delenv(key, raising=True)
    with pytest.raises(ImportError):
        importlib.reload(magic)


def test_import_magic():
    import magic

    assert magic
