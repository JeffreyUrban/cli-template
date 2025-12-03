# Performance Guidance

Performance optimization strategies and profiling techniques.

**Inherits from:** [../CLAUDE.md](../CLAUDE.md) - Read universal rules first

---

## Philosophy

**Profile before optimizing** - Don't optimize without measuring.

**Document complexity** - Time/space complexity for critical algorithms should be documented in dev-docs.

---

## Performance Documentation

### Time/Space Complexity

**Document in dev-docs/design/ALGORITHM_DESIGN.md:**
```markdown
## Algorithm Complexity

### parse_input()
- **Time:** O(n) where n is input length
- **Space:** O(n) for parsed output
- **Trade-off:** Could reduce space to O(1) but would require streaming
```

---

## Performance Testing

*Add performance test patterns if needed*

```python
@pytest.mark.slow
@pytest.mark.performance
def test_large_input_performance():
    """Verify performance with large input."""
    large_data = generate_large_dataset()

    import time
    start = time.time()
    result = process(large_data)
    duration = time.time() - start

    assert duration < 1.0  # Should complete in < 1 second
```

---

## Next Steps

**Related guidance:**
- [Development](./development.md) - Code patterns
- [Testing](./testing.md) - Performance tests
- [Troubleshooting](./troubleshooting.md) - Profiling techniques
