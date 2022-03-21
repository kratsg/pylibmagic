"""
Copyright (c) 2022 Giordon Stark. All rights reserved.

pylibmagic: scikit-build project with CMake for compiling libmagic
"""


from __future__ import annotations

import ctypes
import os
import sys

from ._version import version as __version__

if sys.version_info >= (3, 9):
    from importlib import resources
else:
    import importlib_resources as resources
data = resources.files(__name__)

# structure below matches https://github.com/python/cpython/blob/b3f2d4c8bab52573605c96c809a1e2162eee9d7e/Lib/ctypes/util.py
keys: list[str] = []
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

os.environ[
    "MAGIC"
] = f"{data.joinpath('magic.mgc')}{os.pathsep}{os.environ.get('MAGIC', '')}"

# linux is buggy, it does not return full paths via find_library
# and python-magic hard-codes this as well:
#   https://github.com/ahupp/python-magic/blob/0fb1922da4a7b27bd19b75a03dca2f51bff4362f/magic/loader.py#L32-L34
# But we shouldn't blame python-magic here. We should blame python:
#   - https://bugs.python.org/issue18502
#   - https://bugs.python.org/issue21042
# since reasonable, rational people expect consistency across platforms in python... but ok...
if sys.platform == "linux":

    setattr(ctypes.CDLL, "__init_orig__", ctypes.CDLL.__init__)  # noqa: B010

    # for python 3.7
    if sys.version_info < (3, 8):

        def __magic_init__(
            self: ctypes.CDLL,
            name: str | None,
            mode: int = ctypes.DEFAULT_MODE,
            handle: int | None = None,
            use_errno: bool = False,
            use_last_error: bool = False,
        ) -> None:
            if name:
                path = data / name
                if path.is_file():
                    name = str(path)
            self.__init_orig__(
                name,
                mode=mode,
                handle=handle,
                use_errno=use_errno,
                use_last_error=use_last_error,
            )

    else:

        def __magic_init__(
            self: ctypes.CDLL,
            name: str | None,
            mode: int = ctypes.DEFAULT_MODE,
            handle: int | None = None,
            use_errno: bool = False,
            use_last_error: bool = False,
            winmode: int | None = None,
        ) -> None:
            if name:
                path = data / name
                if path.is_file():
                    name = str(path)
            self.__init_orig__(
                name,
                mode=mode,
                handle=handle,
                use_errno=use_errno,
                use_last_error=use_last_error,
                winmode=winmode,
            )

    setattr(ctypes.CDLL, "__init__", __magic_init__)  # noqa: B010

__all__ = ("__version__", "data", "keys")
