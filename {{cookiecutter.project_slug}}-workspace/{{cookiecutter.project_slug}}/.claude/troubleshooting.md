# Troubleshooting & Debugging Guidance

Debugging techniques, common issues, and problem-solving strategies.

**Inherits from:** [../CLAUDE.md](../CLAUDE.md) - Read universal rules first

---

## Philosophy

**Fail loudly** - Don't hide when things don't work. Make errors visible and actionable.

**Investigate root causes** - Find proper solutions, not workarounds.

---

## Common Issues & Solutions

### Rich Output Formatting in Tests

**Issue:** Rich output varies with terminal width, causing test failures

**Solution:** Set COLUMNS environment variable
```python
@pytest.mark.unit
def test_cli_output():
    """Test CLI output with consistent formatting."""
    # Set in test
    import os
    os.environ['COLUMNS'] = '120'

    # Or in pytest fixture / conftest.py
    result = cli_command()
    assert "expected" in result
```

**In CI:** Add to test command in `.github/workflows/test.yml`:
```yaml
env:
  COLUMNS: 120
```

---

## Debugging Techniques

### Pytest Debugging

**Run single test with verbose output:**
```bash
pytest tests/test_module.py::test_function -vv
```

**Stop at first failure:**
```bash
pytest -x
```

**Run only last failed tests:**
```bash
pytest --lf
```

**Show local variables on failure:**
```bash
pytest -l
```

---

## Error Investigation

### Stack Trace Analysis

**Read from bottom to top:**
1. Bottom: Where error occurred
2. Middle: Call stack
3. Top: Entry point

**Focus on your code first** - Framework/library traces often point to your code's misuse

### Common Error Patterns

*Add project-specific error patterns here as they're discovered*

---

## Performance Issues

**Profile before optimizing:**
```bash
python -m cProfile -o profile.stats script.py
python -m pstats profile.stats
```

**Or use py-spy for live profiling:**
```bash
py-spy top -- python script.py
```

---

## Environment Issues

### Virtual Environment

**Check active venv:**
```bash
which python
python --version
```

**Recreate if needed:**
```bash
rm -rf .venv
uv venv
source .venv/bin/activate
uv pip install -e ".[dev,docs]"
```

### Dependency Conflicts

**Check installed versions:**
```bash
uv pip list
```

**Regenerate lock file:**
```bash
rm uv.lock
uv pip install -e ".[dev,docs]"
```

---

## CI/CD Issues

### Tests Pass Locally, Fail in CI

**Common causes:**
1. Environment differences (COLUMNS, timezone, etc.)
2. Missing dependencies in CI
3. File permissions
4. Timing/ordering issues

**Investigation:**
1. Check CI logs carefully
2. Reproduce CI environment locally (same Python version)
3. Add debug output temporarily
4. Check for environment-specific behavior

### GitHub Actions Debugging

**Add debug output:**
```yaml
- name: Debug info
  run: |
    echo "Python: $(python --version)"
    echo "Working dir: $(pwd)"
    ls -la
```

---

## Tool-Specific Issues

*Add tool-specific debugging guidance as patterns emerge*

### ruff

**Check specific file:**
```bash
ruff check path/to/file.py
ruff check path/to/file.py --fix
```

### mypy

**Check with verbose output:**
```bash
mypy src/ --show-error-codes --pretty
```

---

## Next Steps

**Related guidance:**
- [Development](./development.md) - Error handling patterns
- [Testing](./testing.md) - Test debugging
- [Workflows](./workflows/) - Bug fixing workflow
