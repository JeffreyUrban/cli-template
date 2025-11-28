"""Tests for CLI statistics printing."""

import pytest

from {{ cookiecutter.package_name }}.cli import print_stats
from {{ cookiecutter.package_name }}.{{ cookiecutter.package_name }} import {{ cookiecutter.class_name }}


@pytest.mark.unit
def test_print_stats_normal():
    """Test print_stats with normal processor."""
    processor = {{ cookiecutter.class_name }}()

    # print_stats writes to stderr via rich Console
    # Just verify it doesn't crash
    print_stats(processor)


@pytest.mark.unit
def test_print_stats_empty():
    """Test print_stats with no lines processed."""
    processor = {{ cookiecutter.class_name }}()

    # print_stats should handle empty stats
    print_stats(processor)
