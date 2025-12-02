# Feature Development Workflow

Step-by-step workflow for developing new features.

**Inherits from:** [../../CLAUDE.md](../../CLAUDE.md) - Read universal rules first

---

## Before You Start

**Read relevant guidance:**
- [Development](../development.md) - Code standards
- [Testing](../testing.md) - Test requirements
- [Documentation](../documentation.md) - Doc requirements

**Understand the requirement:**
1. Clarify scope with user
2. Review related design docs
3. Check for existing patterns

---

## Workflow

### 1. Plan (if complex)

For complex features requiring multiple approaches or significant changes, use EnterPlanMode:
- Explore codebase
- Design implementation approach
- Get user approval before implementing

For simple features, proceed directly to implementation.

### 2. Document Design (if needed)

**Update design docs:**
- `dev-docs/design/IMPLEMENTATION.md` - Implementation approach
- `dev-docs/design/DESIGN_RATIONALE.md` - Why this approach

**Create todo list:**
Use TodoWrite to track implementation steps.

### 3. Write Tests (TDD approach)

**Create test file:**
```bash
tests/test_new_feature.py
```

**Write failing tests:**
```python
import pytest
from {{ cookiecutter.project_slug }} import new_feature

@pytest.mark.unit
def test_new_feature_basic():
    """Test basic functionality."""
    result = new_feature.process("input")
    assert result == "expected"

@pytest.mark.unit
def test_new_feature_edge_case():
    """Test edge case."""
    result = new_feature.process("")
    assert result is None
```

**Run tests (should fail):**
```bash
pytest tests/test_new_feature.py
```

### 4. Implement Feature

**Create module:**
```python
# src/{{ cookiecutter.project_slug }}/new_feature.py

def process(input: str) -> str | None:
    """Process input and return result.

    Args:
        input: Input string to process

    Returns:
        Processed result or None if empty
    """
    if not input:
        return None
    return f"processed: {input}"
```

**Run tests (should pass):**
```bash
pytest tests/test_new_feature.py
```

### 5. Update CLI (if needed)

**Add command to cli.py:**
```python
@app.command()
def new_feature(
    input: str = typer.Argument(..., help="Input value"),
):
    """Description of new feature."""
    result = process(input)
    if result:
        console.print(f"[green]{result}[/green]")
```

**Test CLI:**
```bash
{{ cookiecutter.command_name }} new-feature "test"
```

### 6. Update Documentation

**User documentation:**
- Add feature description to `docs/features/`
- Add example to `docs/examples/`
- Update `docs/reference/cli.md` if CLI changed

**Example:**
````markdown
## New Feature

Description of what it does.

### Usage

\```console
$ {{ cookiecutter.command_name }} new-feature "input"
processed: input
\```

### Examples

Basic usage:
\```console
$ {{ cookiecutter.command_name }} new-feature "hello"
processed: hello
\```
````

**Design documentation:**
- Update `dev-docs/design/IMPLEMENTATION.md` if architecture changed

### 7. Run Quality Checks

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/{{ cookiecutter.project_slug }}

# Lint
ruff check .

# Format
ruff format .

# Type check
mypy src/{{ cookiecutter.project_slug }}

# Test documentation
pytest docs/
```

### 8. Verify Everything

**Checklist:**
- [ ] Tests pass
- [ ] Coverage maintained or improved
- [ ] Linter passes
- [ ] Type checker passes
- [ ] Documentation updated
- [ ] Doc examples tested
- [ ] Feature works end-to-end

### 9. Commit (if user requests)

Only create commits when user asks. See main CLAUDE.md for commit workflow.

---

## Common Patterns

### Adding CLI Option

```python
@app.command()
def existing_command(
    new_option: bool = typer.Option(False, "--new-option", help="Description"),
):
    """Command description."""
    if new_option:
        # Handle new option
        pass
```

### Adding Configuration

```python
from dataclasses import dataclass

@dataclass
class Config:
    """Configuration for {{ cookiecutter.project_slug }}."""
    new_setting: bool = False

def process(input: str, config: Config) -> str:
    """Process with configuration."""
    if config.new_setting:
        # Use new setting
        pass
```

---

## Anti-Patterns to Avoid

**Don't:**
- Implement before understanding requirements
- Skip tests ("I'll add them later")
- Over-engineer the solution
- Add features not requested
- Break existing functionality
- Skip documentation

**Do:**
- Clarify requirements first
- Write tests alongside code
- Keep solutions simple
- Implement only what's requested
- Run regression tests
- Document as you go

---

## Troubleshooting

### Tests Failing

1. Check if test expectations are correct
2. Run single test with `-vv` for details
3. Add debug prints temporarily
4. Verify fixtures and test data

### Type Checker Errors

1. Add type hints to new code
2. Import types from `typing` if needed
3. Use `typing.cast()` for type narrowing
4. Check for `Any` types and make more specific

### Documentation Not Rendering

1. Check markdown syntax
2. Verify code block fences
3. Run `mkdocs serve` to preview
4. Check for broken links

---

## Next Steps

**After feature is complete:**
- Mark todos as completed
- Clean up any debug code
- Remove temporary comments
- Update CHANGELOG if project has one

**Related workflows:**
- [Bug Fixing](./bug-fixing.md) - Fixing bugs
- [Releasing](./releasing.md) - Release process
