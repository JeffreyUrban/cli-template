# Testing Guidance

Test strategy, pytest patterns, coverage requirements, and quality standards.

**Inherits from:** [../CLAUDE.md](../CLAUDE.md) - Read universal rules first

## Quick Reference

**Framework:** pytest (exclusively - not unittest)
**Markers:** `@pytest.mark.unit`, `@pytest.mark.integration`, `@pytest.mark.slow`
**Coverage:** Measured with pytest-cov, target 0% initially (increase as project matures)
**Philosophy:** Testing is not optional - all features require tests

---

## Core Principles

**1. Testing is required** - All features must have tests before completion

**2. Use pytest exclusively** - Not unittest, only pytest

**3. Organize with markers** - Tag tests by type for selective running

**4. Tests are documentation** - Clear test names explain expected behavior

---

## Test Organization

### Directory Structure

```
tests/
├── conftest.py           # Shared fixtures
├── fixtures/             # Test data
│   ├── input/           # Input files for tests
│   └── expected/        # Expected output files
├── unit/                 # Unit tests (if many tests)
├── integration/          # Integration tests (if many tests)
└── test_*.py            # Test modules
```

**Principles:**
- Mirror `src/` structure in test file names
- `test_module.py` tests `module.py`
- Keep related tests together

### Test File Template

```python
"""Tests for module_name.

Description of what's being tested and why.
"""

import pytest
from {{ cookiecutter.project_slug }} import ModuleName


# Fixtures specific to this test module
@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {...}


# Unit tests
@pytest.mark.unit
def test_basic_functionality(sample_data):
    """Test basic functionality with valid input."""
    result = ModuleName.process(sample_data)
    assert result == expected


@pytest.mark.unit
def test_edge_case():
    """Test edge case: empty input."""
    result = ModuleName.process("")
    assert result is None


# Integration tests
@pytest.mark.integration
def test_full_workflow(tmp_path):
    """Test complete workflow from input to output."""
    # Setup
    input_file = tmp_path / "input.txt"
    input_file.write_text("test data")

    # Execute
    result = ModuleName.process_file(input_file)

    # Verify
    assert result.success
    assert result.output == expected_output
```

---

## Pytest Markers

**Use markers to organize tests:**

```python
import pytest

@pytest.mark.unit
def test_pure_function():
    """Fast, isolated unit test."""
    ...

@pytest.mark.integration
def test_system_integration():
    """Tests multiple components together."""
    ...

@pytest.mark.slow
def test_performance():
    """Long-running test."""
    ...

@pytest.mark.parametrize("input,expected", [
    ("case1", "result1"),
    ("case2", "result2"),
])
def test_multiple_cases(input, expected):
    """Test multiple cases efficiently."""
    assert process(input) == expected
```

**Running specific markers:**
```bash
pytest -m unit              # Only unit tests
pytest -m "not slow"        # Skip slow tests
pytest -m "unit or integration"  # Multiple markers
```

---

## Fixtures

### Shared Fixtures (conftest.py)

```python
"""Shared pytest fixtures for all tests."""

import pytest
from pathlib import Path


@pytest.fixture
def fixtures_dir():
    """Path to test fixtures directory."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_input(fixtures_dir):
    """Load sample input file."""
    return (fixtures_dir / "input" / "sample.txt").read_text()


@pytest.fixture
def expected_output(fixtures_dir):
    """Load expected output file."""
    return (fixtures_dir / "expected" / "sample.txt").read_text()
```

### Module-Specific Fixtures

Define in test file for fixtures used only in that module:

```python
@pytest.fixture
def configured_instance():
    """Create configured instance for tests."""
    instance = MyClass(param=value)
    instance.setup()
    yield instance
    instance.cleanup()  # Teardown
```

---

## Test Patterns

### Testing CLI Commands

```python
from typer.testing import CliRunner
from {{ cookiecutter.project_slug }}.cli import app

runner = CliRunner()

@pytest.mark.unit
def test_cli_basic():
    """Test basic CLI invocation."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.stdout


@pytest.mark.integration
def test_cli_with_file(tmp_path):
    """Test CLI with file input."""
    input_file = tmp_path / "input.txt"
    input_file.write_text("test data")

    result = runner.invoke(app, [str(input_file)])
    assert result.exit_code == 0
    assert "Success" in result.stdout
```

### Testing File Operations

```python
@pytest.mark.integration
def test_file_processing(tmp_path):
    """Test file processing end-to-end."""
    # Setup input
    input_file = tmp_path / "input.txt"
    input_file.write_text("test\ndata\n")

    # Process
    output_file = tmp_path / "output.txt"
    process_file(input_file, output_file)

    # Verify
    assert output_file.exists()
    assert output_file.read_text() == "expected\noutput\n"
```

### Testing Exceptions

```python
@pytest.mark.unit
def test_invalid_input_raises():
    """Test that invalid input raises appropriate error."""
    with pytest.raises(ValueError, match="invalid input"):
        process(invalid_data)
```

### Parametrized Tests

```python
@pytest.mark.unit
@pytest.mark.parametrize("input,expected", [
    ("", ""),
    ("single", "single"),
    ("multiple\nlines", "multiple\nlines"),
    pytest.param("slow_case", "result", marks=pytest.mark.slow),
])
def test_multiple_cases(input, expected):
    """Test various input cases."""
    assert process(input) == expected
```

---

## Coverage

### Running with Coverage

```bash
# Run all tests with coverage
pytest --cov=src/{{ cookiecutter.project_slug }} --cov-report=term --cov-report=html

# Fail if coverage below threshold
pytest --cov=src/{{ cookiecutter.project_slug }} --cov-fail-under=0

# View HTML report
open htmlcov/index.html
```

### Coverage Configuration

In `pyproject.toml`:
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
markers = [
    "unit: Unit tests",
    "integration: Integration tests",
    "slow: Slow tests",
]

[tool.coverage.run]
source = ["src"]
omit = [
    "*/tests/*",
    "*/__pycache__/*",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
]
```

### Coverage Targets

**Initial:** 0% - don't block on coverage initially
**Growth:** Increase gradually as project matures
**Target:** 80%+ for production code

**Focus on:**
- Critical business logic
- Edge cases and error handling
- Public APIs

**Don't stress about:**
- Simple getters/setters
- Trivial utility functions
- Type checking blocks (`if TYPE_CHECKING:`)

---

## Test Debugging

### When Tests Fail

**1. Understand the failure:**
```bash
pytest -vv  # Verbose output
pytest --tb=short  # Shorter traceback
pytest -x  # Stop at first failure
pytest --lf  # Run only last failed
```

**2. Determine if it's a fix or regression:**
- **Fix:** Test was wrong, update it
- **Regression:** Code broke, fix the code

**3. Isolate the issue:**
```bash
pytest tests/test_specific.py::test_function  # Run single test
pytest -k "keyword"  # Run tests matching keyword
```

### Debugging Tips

```python
# Add print statements (removed before commit)
def test_debug():
    result = process(data)
    print(f"DEBUG: result = {result}")  # Temporary
    assert result == expected

# Use pytest's built-in debugging
def test_with_breakpoint():
    result = process(data)
    breakpoint()  # Opens debugger
    assert result == expected
```

---

## Common Test Mistakes

### ❌ Don't: Test implementation details

```python
# Bad - tests internal implementation
def test_internal_cache():
    obj = MyClass()
    obj.process(data)
    assert obj._cache == {...}  # Internal detail
```

### ✅ Do: Test observable behavior

```python
# Good - tests public interface
def test_processing_result():
    obj = MyClass()
    result = obj.process(data)
    assert result == expected
```

### ❌ Don't: Write tests that depend on each other

```python
# Bad - order-dependent tests
def test_step1():
    global state
    state = process()

def test_step2():
    assert state == expected  # Depends on test_step1
```

### ✅ Do: Make tests independent

```python
# Good - each test is independent
def test_step1():
    state = process()
    assert state is not None

def test_step2():
    state = process()  # Create own state
    assert state == expected
```

---

## Test Data Management

### Fixture Files

**Organize fixtures:**
```
tests/fixtures/
├── input/
│   ├── simple.txt
│   ├── complex.json
│   └── edge-case.txt
└── expected/
    ├── simple-output.txt
    ├── complex-output.json
    └── edge-case-output.txt
```

**Load fixtures:**
```python
@pytest.fixture
def fixtures_dir():
    return Path(__file__).parent / "fixtures"

def test_with_fixture(fixtures_dir):
    input_data = (fixtures_dir / "input" / "simple.txt").read_text()
    expected = (fixtures_dir / "expected" / "simple-output.txt").read_text()

    result = process(input_data)
    assert result == expected
```

### Generated Test Data

```python
import pytest
from hypothesis import given, strategies as st

@given(st.text())
def test_property_based(input_text):
    """Test property: output length <= input length."""
    result = process(input_text)
    assert len(result) <= len(input_text)
```

---

## CI/CD Integration

Tests run automatically in GitHub Actions:

```yaml
# .github/workflows/test.yml
- name: Run tests with coverage
  run: |
    pytest --cov=src/{{ cookiecutter.project_slug }} --cov-report=xml --cov-fail-under=0
```

**All tests must pass before merging.**

---

## Next Steps

**Related guidance:**
- [Development](./development.md) - Code standards and patterns
- [Documentation](./documentation.md) - Doc testing with Sybil
- [Workflows](./workflows/) - Task-specific workflows

**Related documentation:**
- [TESTING_STRATEGY.md](../dev-docs/testing/TESTING_STRATEGY.md) - Detailed test strategy
- [TEST_COVERAGE.md](../dev-docs/testing/TEST_COVERAGE.md) - Coverage plan
