from __future__ import annotations

import pytest


@pytest.mark.isolate
def test_import_magic_fail():
    with pytest.raises(ImportError):
        import magic  # nopycln: import # noqa: F401
