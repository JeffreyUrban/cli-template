# Development Guidance

Coding standards, patterns, tools, and modern practices for this project.

**Inherits from:** [../CLAUDE.md](../CLAUDE.md) - Read universal rules first

## Quick Reference

**Language:** Python {{ cookiecutter.python_version }}+
**Code Quality:** ruff (lint + format) + mypy
**Style:** Type hints required, docstrings for public APIs
**Philosophy:** Modern, mature tools over legacy approaches

---

## Code Standards

### Type Hints

**Required** for all function signatures:

```python
def process_data(input: str, count: int = 10) -> list[str]:
    """Process input data and return results."""
    ...
```

**Not required** for:
- Private helper functions (internal use only)
- Simple lambdas where types are obvious from context

### Docstrings

**Required** for:
- Public functions and classes
- Modules (top-level docstring)
- Complex internal functions

**Format:** Google style

```python
def example(param1: str, param2: int) -> bool:
    """Short one-line summary.

    Longer description if needed, explaining purpose and usage.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When input is invalid
    """
```

### Constants and Magic Numbers

**Avoid magic numbers** - use named constants:

```python
# Bad
if value > 0.85:
    ...

# Good
CONFIDENCE_THRESHOLD = 0.85
if value > CONFIDENCE_THRESHOLD:
    ...
```

---

## Modern Tools & Techniques

**Philosophy:** Favor modern, mature tools over legacy approaches. Not bleeding edge, but proven improvements.

### Python Libraries

**Project standards:**
- **CLI tools:** `typer` (type-based, modern) over `argparse`/`click`
- **Terminal output:** `rich` for beautiful CLI output, progress bars, tables
- **HTTP client:** `httpx` over `requests` (if needed)
- **Date/time:** `datetime` standard library (avoid `arrow`/`pendulum` unless needed)

**Consider when relevant:**
- **Validation:** `pydantic` for data validation
- **Async:** `asyncio` + `httpx` for concurrent operations
- **Serialization:** `pydantic` or `dataclasses` with type hints

### Code Quality Tools

**ruff** - Linter and formatter (replaces black, flake8, isort):
```bash
ruff check .        # Lint
ruff format .       # Format
```

**mypy** - Type checker:
```bash
mypy src/{{ cookiecutter.project_slug }}
```

**Pre-commit** - Runs checks before commit:
```bash
pre-commit install  # One-time setup
pre-commit run --all-files  # Manual run
```

---

## Architecture Patterns

### Project Structure

```
src/{{ cookiecutter.project_slug }}/
├── __init__.py           # Package initialization, version
├── cli.py                # CLI interface (typer + rich)
├── {{ cookiecutter.project_slug }}.py  # Core logic
└── utils.py              # Shared utilities (if needed)
```

**Principles:**
- Keep `cli.py` focused on CLI interface only
- Put business logic in separate modules
- Use clear module names that describe their purpose

### Error Handling

**User-facing errors** (CLI):
```python
import typer

if invalid_input:
    raise typer.BadParameter("Clear message about what's wrong")
```

**Internal errors** (library code):
```python
if error_condition:
    raise ValueError("Descriptive error message")
```

**Never silently fail** - always raise or log errors.

---

## Complexity Guidelines

### Avoid Over-Engineering

**Key principle:** Only make changes that are directly requested or clearly necessary. Keep solutions simple and focused.

**Don't:**
- Add features, refactor, or make "improvements" beyond what was asked
- Add error handling for scenarios that can't happen
- Create abstractions for one-time operations
- Design for hypothetical future requirements
- Add docstrings/comments/type annotations to unchanged code

**Do:**
- Trust internal code and framework guarantees
- Only validate at system boundaries (user input, external APIs)
- Three similar lines is better than premature abstraction
- If something is unused, delete it completely (no backwards-compatibility hacks)

**Examples of over-engineering to avoid:**
- Using feature flags or compatibility shims when you can just change the code
- Adding helpers/utilities for operations that happen once
- Creating configuration for values that never change
- Renaming unused `_vars`, re-exporting removed types, adding `# removed` comments

---

## Security Best Practices

**Always check for:**
- Command injection vulnerabilities
- SQL injection (use parameterized queries)
- XSS vulnerabilities
- Path traversal issues
- OWASP Top 10 vulnerabilities

**If you notice insecure code:**
- Immediately fix it
- Document the vulnerability in commit message
- Add tests to prevent regression

---

## Performance Considerations

**Profile before optimizing:**
- Don't optimize without measuring
- Use `cProfile` or `py-spy` for profiling
- Document performance requirements in dev-docs

**Time/Space Complexity:**
- Document in dev-docs for critical algorithms
- Add comments for non-obvious complexity tradeoffs

---

## Tool Usage (Claude-Specific)

### File Operations

**Always use dedicated tools:**
- **Read** - Read files (not `cat`/`head`/`tail`)
- **Edit** - Edit files (not `sed`/`awk`)
- **Write** - Create files (not `echo >/cat <<EOF`)
- **Glob** - Find files (not `find`/`ls`)
- **Grep** - Search content (not `grep`/`rg`)

**Reserve Bash for:**
- Git operations
- Package management (uv, pip)
- Running tests/linters
- Process management

### Parallel Operations

**Run independent operations in parallel:**

```xml
<!-- Good: Parallel reads -->
<Read file="file1.py"/>
<Read file="file2.py"/>
<Grep pattern="TODO"/>

<!-- Bad: Sequential when not needed -->
<Read file="file1.py"/>
<!-- wait -->
<Read file="file2.py"/>
```

**Run dependent operations sequentially:**
- Use `&&` to chain commands that depend on each other
- Use `;` only when you don't care if earlier commands fail

---

## Common Patterns

### CLI Interface (typer)

```python
import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def main(
    input_file: Path = typer.Argument(..., help="Input file path"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
):
    """Command description."""
    if verbose:
        console.print("[yellow]Processing...[/yellow]")

    # Logic here
```

### Rich Output

```python
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

# Simple output
console.print("[green]Success![/green]")

# Tables
table = Table(title="Results")
table.add_column("Name")
table.add_column("Value")
table.add_row("Item", "123")
console.print(table)

# Progress bars
for item in track(items, description="Processing..."):
    process(item)
```

---

## IDE Configuration

**PyCharm:**
- Project settings pre-configured in `.idea/`
- Source roots automatically set
- Run configurations in `.run/`

**VS Code:**
- Settings pre-configured in `.vscode/settings.json`
- Includes pytest, ruff, mypy configuration

---

## Next Steps

**Related guidance:**
- [Testing](.//testing.md) - Test standards and patterns
- [Documentation](./documentation.md) - Documentation standards
- [Workflows](./workflows/) - Common task workflows

**Related documentation:**
- [IMPLEMENTATION.md](../dev-docs/design/IMPLEMENTATION.md) - Implementation details
- [DESIGN_RATIONALE.md](../dev-docs/design/DESIGN_RATIONALE.md) - Design decisions
