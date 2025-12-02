# Bug Fixing Workflow

Step-by-step workflow for identifying and fixing bugs.

**Inherits from:** [../../CLAUDE.md](../../CLAUDE.md) - Read universal rules first

---

## Workflow

### 1. Reproduce the Bug

**Understand the issue:**
- What is the expected behavior?
- What is the actual behavior?
- How to reproduce?

**Create minimal reproduction:**
```python
# Minimal code that demonstrates the bug
from {{ cookiecutter.project_slug }} import problematic_function

result = problematic_function("input that causes bug")
# Expected: X
# Actual: Y
```

### 2. Write a Failing Test

**Create test that demonstrates the bug:**
```python
@pytest.mark.unit
def test_bug_description():
    """Test for bug: brief description."""
    result = problematic_function("input")
    assert result == expected  # This should fail
```

**Verify test fails:**
```bash
pytest tests/test_module.py::test_bug_description -v
```

### 3. Investigate Root Cause

**Use debugging tools:**
```python
# Add temporary debug output
print(f"DEBUG: variable = {variable}")

# Or use breakpoint
breakpoint()

# Run test
pytest tests/test_module.py::test_bug_description -s
```

**Common investigation steps:**
1. Check input validation
2. Verify algorithm logic
3. Look for edge cases
4. Check state/side effects
5. Review recent changes

### 4. Fix the Bug

**Implement fix:**
- Make minimal changes
- Fix root cause, not symptoms
- Maintain existing behavior for other cases

**Example:**
```python
def fixed_function(input: str) -> str:
    """Fixed version."""
    # Previous code had bug here
    if not input:  # Add missing edge case handling
        return ""

    return process(input)
```

### 5. Verify Fix

**Test passes:**
```bash
pytest tests/test_module.py::test_bug_description
```

**Run related tests:**
```bash
pytest tests/test_module.py
```

**Run all tests (regression check):**
```bash
pytest
```

### 6. Clean Up

**Remove debug code:**
- Delete print statements
- Remove breakpoints
- Clean up temporary changes

**Update tests if needed:**
- Keep the bug test
- Add more edge case tests if discovered

### 7. Document (if significant)

**Update documentation if:**
- Behavior changed
- Edge case handling changed
- Fix affects public API

**Add to CHANGELOG:**
```markdown
### Fixed
- Fixed bug where X caused Y (#issue-number)
```

---

## Common Bug Patterns

### Off-by-One Errors

```python
# Bug
for i in range(len(items) - 1):  # Misses last item
    process(items[i])

# Fix
for i in range(len(items)):
    process(items[i])

# Better: Use iteration
for item in items:
    process(item)
```

### Edge Cases

```python
# Bug: Doesn't handle empty input
def process(data: list) -> str:
    return data[0]  # IndexError if empty

# Fix: Handle edge case
def process(data: list) -> str:
    if not data:
        return ""
    return data[0]
```

### Type Errors

```python
# Bug: Assumes input type
def process(value):
    return value.strip()  # AttributeError if not string

# Fix: Validate type
def process(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"Expected str, got {type(value)}")
    return value.strip()
```

---

## Debugging Techniques

### Print Debugging

```python
def debug_function(input):
    print(f"DEBUG: input = {input}")
    result = process(input)
    print(f"DEBUG: result = {result}")
    return result
```

### Breakpoint Debugging

```python
def debug_function(input):
    breakpoint()  # Opens pdb debugger
    result = process(input)
    return result
```

### Test-Driven Debugging

1. Write test that fails
2. Run test to see failure
3. Fix code
4. Run test to verify
5. Repeat until passing

---

## Prevention

**After fixing a bug:**

1. **Add test** - Prevent regression
2. **Look for similar bugs** - Same pattern elsewhere?
3. **Update validation** - Can we catch this earlier?
4. **Document edge cases** - Update design docs if needed

---

## Troubleshooting

### Can't Reproduce

- Try different environments
- Check version dependencies
- Verify input data exactly matches
- Look for timing/state issues

### Fix Breaks Other Tests

- Regression - fix broke existing functionality
- Analyze what changed
- May need different approach
- Consider if original tests are correct

### Can't Find Root Cause

- Simplify reproduction
- Binary search (comment out code)
- Check assumptions
- Ask for help (create detailed issue)

---

## Next Steps

**After fix is verified:**
- Remove debug code
- Update documentation if needed
- Consider if similar bugs exist
- Mark todos as completed

**Related workflows:**
- [Feature Development](./feature-development.md) - Adding features
- [Releasing](./releasing.md) - Release process
