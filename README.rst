pylibmagic v0.5.0
=================

A lightweight, minimal python package that ships ``magic`` libraries
using automake, CMake, scikit-build, and cibuildwheel.

|Actions Status| |Cirrus Status| |Documentation Status| |Code style: black|

|PyPI version| |PyPI platforms|

|GitHub Discussion| |Gitter|

Why?
----

If you use `python-magic <https://github.com/ahupp/python-magic>`__, you typically get an error like this

.. code:: pycon

   >>> import magic
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "/Users/kratsg/.pyenv/versions/venv/lib/python3.7/site-packages/magic/__init__.py", line 209, in <module>
       libmagic = loader.load_lib()
     File "/Users/kratsg/.pyenv/versions/venv/lib/python3.7/site-packages/magic/loader.py", line 49, in load_lib
       raise ImportError('failed to find libmagic.  Check your installation')
   ImportError: failed to find libmagic.  Check your installation

which is frustrating because they don’t ship shared lib with their
python distribution. ``pylibmagic`` helps fill in the missing gap by
shipping the required ``magic`` library and adding it to your path, so
you can just do:

.. code:: pycon

   >>> import pylibmagic
   >>> import magic

and be on your way. ``pylibmagic`` is designed to be very minimal and
lightweight.

Compiling
---------

.. code:: bash

   $ docker run -it --rm -v $PWD:/home/root -w /home/root ubuntu
   # apt install cmake autoconf automake libtool build-essential git python3-dev python3-pip
   # cmake -S . -B build
   # cmake --build build

Installing
----------

.. code:: bash

   $ python3 -m pip install pylibmagic

and the libraries are installed at

.. code:: bash

    $ python -c "import pylibmagic; print(pylibmagic.data)"


Releasing
---------

To release, due to concurrency issues, we need to push the tag after Cirrus CI finishes with the building for pushing to the main branch. So the order is typically:

.. code:: bash

   tbump 0.5.0 --no-tag-push
   # wait until Cirrus CI finishes
   git push origin v0.5.0
   # wait until Cirrus CI finishes
   gh release create

See [cirruslabs/cirrus-ci-docs#1167](https://github.com/cirruslabs/cirrus-ci-docs/issues/1167) for more details.

.. |Actions Status| image:: https://github.com/kratsg/pylibmagic/workflows/CI/badge.svg
   :target: https://github.com/kratsg/pylibmagic/actions
.. |Cirrus Status| image:: https://api.cirrus-ci.com/github/kratsg/pylibmagic.svg?branch=main
   :target: https://cirrus-ci.com/github/kratsg/pylibmagic
.. |Documentation Status| image:: https://readthedocs.org/projects/pylibmagic/badge/?version=latest
   :target: https://pylibmagic.readthedocs.io/en/latest/?badge=latest
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |PyPI version| image:: https://badge.fury.io/py/pylibmagic.svg
   :target: https://pypi.org/project/pylibmagic/
.. |PyPI platforms| image:: https://img.shields.io/pypi/pyversions/pylibmagic
   :target: https://pypi.org/project/pylibmagic/
.. |GitHub Discussion| image:: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
   :target: https://github.com/kratsg/pylibmagic/discussions
.. |Gitter| image:: https://badges.gitter.im/https://github.com/kratsg/pylibmagic/community.svg
   :target: https://gitter.im/https://github.com/kratsg/pylibmagic/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
