"""
Copyright (c) 2022 Giordon Stark. All rights reserved.

pylibmagic: scikit-build project with CMake for compiling libmagic
"""


from __future__ import annotations

import os
import sys

from ._version import version as __version__

if sys.version_info >= (3, 9):
    from importlib import resources
else:
    import importlib_resources as resources
data = resources.files(__name__)

# structure below matches https://github.com/python/cpython/blob/b3f2d4c8bab52573605c96c809a1e2162eee9d7e/Lib/ctypes/util.py
keys = []
if os.name == "nt":
    keys = ["PATH"]
elif os.name == "posix" and sys.platform == "darwin":
    keys = ["DYLD_LIBRARY_PATH"]
elif sys.platform.startswith("aix"):
    keys = ["LD_LIBRARY_PATH"]
elif os.name == "posix":
    keys = ["LIBRARY_PATH", "LD_LIBRARY_PATH"]

if not keys:
    raise OSError(f"{os.name} / {sys.platform} not supported yet.")

for key in keys:
    os.environ[key] = f"{data}{os.pathsep}{os.environ.get(key, '')}"

__all__ = ("__version__", "data")
