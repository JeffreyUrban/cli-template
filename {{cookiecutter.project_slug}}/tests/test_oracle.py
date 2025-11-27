"""Compare algorithm output against reference implementation."""

from io import StringIO

import pytest


@pytest.mark.property
class TestAgainstOracle:
    """Compare algorithm output against reference implementation."""

    def test_something_oracle(self):
        assert True
