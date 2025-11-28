"""Integration tests for end-to-end scenarios."""

from io import StringIO

import pytest

from {{ cookiecutter.package_name }}.{{ cookiecutter.project_slug }} import {{ cookiecutter.class_name }}


@pytest.mark.integration
class TestIntegration:
    """End-to-end integration tests with realistic scenarios."""

    def test_something(self):
        assert True
