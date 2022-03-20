# pylibmagic

Hopefully a python package that ships the libmagic binaries using CMake, scikit-build, and cibuildwheel.

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]
[![Gitter][gitter-badge]][gitter-link]




[actions-badge]:            https://github.com/kratsg/pylibmagic/workflows/CI/badge.svg
[actions-link]:             https://github.com/kratsg/pylibmagic/actions
[black-badge]:              https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]:               https://github.com/psf/black
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/pylibmagic
[conda-link]:               https://github.com/conda-forge/pylibmagic-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/kratsg/pylibmagic/discussions
[gitter-badge]:             https://badges.gitter.im/https://github.com/kratsg/pylibmagic/community.svg
[gitter-link]:              https://gitter.im/https://github.com/kratsg/pylibmagic/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
[pypi-link]:                https://pypi.org/project/pylibmagic/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/pylibmagic
[pypi-version]:             https://badge.fury.io/py/pylibmagic.svg
[rtd-badge]:                https://readthedocs.org/projects/pylibmagic/badge/?version=latest
[rtd-link]:                 https://pylibmagic.readthedocs.io/en/latest/?badge=latest
[sk-badge]:                 https://scikit-hep.org/assets/images/Scikit--HEP-Project-blue.svg


## Compiling

```
docker run -it --rm -v $PWD:/home/root -w /home/root ubuntu
$ apt install cmake autoconf automake libtool build-essential git python3-dev python3-pip
$ cmake -S . -B build
$ cmake --build build
```
