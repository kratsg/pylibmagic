#!/usr/bin/env python
# Copyright (c) 2022, Giordon Stark
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/kratsg/pylibmagic for details.

from __future__ import annotations

from skbuild import setup  # isort:skip

setup(
    packages=["pylibmagic"],
    package_dir={"": "src"},
    cmake_install_dir="src/pylibmagic",
    include_package_data=False,  # see scikit-build/scikit-build#680
)
