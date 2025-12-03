# Performance Guidance

Performance optimization strategies and profiling techniques.

**Inherits from:** [../CLAUDE.md](../CLAUDE.md) - Read universal rules first

---

## Philosophy

**Profile before optimizing** - Don't optimize without measuring.

**Document complexity** - Time/space complexity for critical algorithms should be documented in dev-docs.

---

## When to Optimize

**Optimize when:**
- Performance requirements are documented
- Profiling shows a bottleneck
- User reports performance issues
- Benchmarks show degradation

**Don't optimize when:**
- Code isn't complete
- No performance requirements exist
- No measurements taken
- "It might be slow"

---

## Profiling Tools

### cProfile

**Profile entire script:**
\`\`\`bash
python -m cProfile -o profile.stats script.py
python -m pstats profile.stats
\`\`\`

**In pstats:**
\`\`\`
sort cumtime
stats 10
\`\`\`

### py-spy

**Live profiling:**
\`\`\`bash
pip install py-spy
py-spy top -- python script.py
\`\`\`

**Flame graph:**
\`\`\`bash
py-spy record -o profile.svg -- python script.py
\`\`\`

---

## Common Patterns

*Document performance patterns as they emerge in this project*

### Example: Time/Space Complexity

**Document in dev-docs/design/ALGORITHM_DESIGN.md:**
\`\`\`markdown
## Algorithm Complexity

### parse_input()
- **Time:** O(n) where n is input length
- **Space:** O(n) for parsed output
- **Trade-off:** Could reduce space to O(1) but would require streaming
\`\`\`

---

## Benchmarking

*Add benchmarking approaches as needed*

### pytest-benchmark

\`\`\`python
def test_performance(benchmark):
    """Benchmark critical function."""
    result = benchmark(process_data, large_input)
    assert result is not None
\`\`\`

---

## Optimization Strategies

*Add proven optimization patterns from this project*

### Avoid Premature Optimization

**Bad:**
\`\`\`python
# Optimizing before profiling
def process(items):
    # Complex caching, memoization, etc.
    ...
\`\`\`

**Good:**
\`\`\`python
# Simple, clear implementation first
def process(items):
    return [transform(item) for item in items]

# Profile, then optimize if needed
\`\`\`

---

## Performance Testing

*Add performance test patterns if needed*

\`\`\`python
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
\`\`\`

---

## Next Steps

**Related guidance:**
- [Development](./development.md) - Code patterns
- [Testing](./testing.md) - Performance tests
- [Troubleshooting](./troubleshooting.md) - Profiling techniques
