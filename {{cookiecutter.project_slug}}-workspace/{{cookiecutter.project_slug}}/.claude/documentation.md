# Documentation Guidance

Documentation standards, MkDocs, Sybil, and tested code examples.

**Inherits from:** [../CLAUDE.md](../CLAUDE.md) - Read universal rules first

## Quick Reference

**System:** MkDocs Material
**Doc Testing:** Sybil (tests code examples in docs)
**Location:** `docs/` for user docs, `dev-docs/` for design docs
**Philosophy:** Documentation is code - test it, review it, maintain it

---

## Documentation Types

### 1. User Documentation (`docs/`)

**Purpose:** Help users understand and use the project

**Structure:**
```
docs/
├── index.md              # Landing page
├── getting-started/      # Installation, quick start
├── features/             # Feature descriptions
├── use-cases/            # Real-world examples
├── guides/               # How-to guides
├── reference/            # API reference, CLI reference
└── examples/             # Extended examples with fixtures
    └── fixtures/         # Test data for examples
```

**Audience:** End users of {{ cookiecutter.project_slug }}

**Update when:**
- Adding features
- Changing CLI interface
- Adding examples
- Updating API

### 2. Design Documentation (`dev-docs/`)

**Purpose:** Document technical decisions, architecture, implementation

**Structure:**
```
dev-docs/
├── design/               # Architecture and design
│   ├── IMPLEMENTATION.md
│   ├── ALGORITHM_DESIGN.md
│   └── DESIGN_RATIONALE.md
├── planning/             # Roadmap and planning
│   └── PLANNING.md
└── testing/              # Test strategy
    ├── TESTING_STRATEGY.md
    ├── TEST_COVERAGE.md
    └── ORACLE_TESTING.md
```

**Audience:** Developers, contributors, technical reviewers

**Update when:**
- Changing architecture
- Making design decisions
- Modifying algorithms
- Updating test strategy

### 3. Process Documentation (`.claude/`)

**Purpose:** Guide Claude Code on standards and workflows

**Audience:** Claude instances working on the project

**Update when:** Standards or workflows change

---

## Documentation Philosophy

### Three Types of Documentation

**1. Planning Documentation (temporary)**
- Design explorations
- Implementation plans
- "Next Steps", "TODO" sections
- Archive after completion

**2. Progress Documentation (temporary)**
- "What We've Built"
- Implementation status
- Archive after feature is complete

**3. Work Product Documentation (permanent)**
- Current implementation
- Usage guides
- Architecture decisions
- Keep updated as project evolves

### Key Principles

**Work is not complete until documentation is production-ready**

- Planning/progress docs are valuable during development - archive after completion
- Work product docs describe current reality, not plans or history
- Put function details in docstrings, not external docs
- Reference code locations, don't duplicate values or implementation
- Preserve design rationales when converting planning → work product docs

**Before creating directory structures:** Discuss scope and organization with user

---

## Documentation-Driven Engineering

**CRITICAL: Before implementing, understand and document requirements first!**

### Workflow

1. **Clarify requirements** through discussion with the user
2. **Document the design** in appropriate work product documentation
3. **Reference the documentation** during implementation
4. **Update documentation** as design evolves

### Documentation Maintenance Rules

| Work Scope | Documentation to Update |
|------------|------------------------|
| **Adding/changing features** | `dev-docs/design/IMPLEMENTATION.md`, `docs/` user guides |
| **Modifying algorithm** | `dev-docs/design/ALGORITHM_DESIGN.md`, `dev-docs/design/IMPLEMENTATION.md` |
| **Adding tests** | `dev-docs/testing/TESTING_STRATEGY.md` |
| **CLI changes** | `README.md`, `docs/reference/cli.md` |
| **Completing milestones** | `dev-docs/planning/PLANNING.md` |
| **Design decisions** | `dev-docs/design/DESIGN_RATIONALE.md` |

### What NOT to Do

**DO NOT:**
- Implement based on assumptions without documented requirements
- Add implementation details to `.claude/*.md` (they belong in `dev-docs/`)
- Skip documentation updates when design changes
- Document violations of requirements as "limitations" or "TODO" items
- Make unsubstantiated causal claims (distinguish observed facts from inferred causes)

---

## MkDocs Standards

### Configuration (mkdocs.yml)

```yaml
site_name: {{ cookiecutter.project_name }}
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - toc.integrate
    - search.suggest
    - content.code.copy

plugins:
  - search
  - autorefs

markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences
  - pymdownx.tabbed
  - admonition
  - toc:
      permalink: true
```

### Writing Documentation

**File naming:**
- Use lowercase with hyphens: `getting-started.md`
- Use descriptive names: `cli-reference.md` not `reference.md`

**Structure:**
```markdown
# Page Title

Brief introduction (1-2 sentences).

## Section

Content with examples.

## Another Section

More content.
```

**Code blocks:**
```markdown
\`\`\`python
# Python code example
from {{ cookiecutter.project_slug }} import example
\`\`\`

\`\`\`console
$ {{ cookiecutter.command_name }} --help
Usage: ...
\`\`\`
```

**Admonitions:**
```markdown
!!! note
    Important information for readers

!!! warning
    Critical warning

!!! tip
    Helpful tip
```

---

## Tested Code Examples (Sybil)

**All code examples in docs are automatically tested!**

### Why Test Documentation?

- Ensures examples actually work
- Catches breaking changes immediately
- Documentation stays in sync with code
- Examples serve as integration tests

### Configuration (docs/conftest.py)

See `docs/conftest.py` for complete configuration. Key features:

- Tests Python and console code blocks
- Supports file verification
- Runs from fixtures directory
- Skips template docs with warning marker

### Writing Testable Python Examples

```markdown
\`\`\`python
from {{ cookiecutter.project_slug }} import process

result = process("input data")
assert result == "expected output"
\`\`\`
```

**Sybil will:**
1. Extract this code block
2. Execute it
3. Fail the test if assertion fails

### Writing Testable Console Examples

```markdown
\`\`\`console
$ echo "test"
test
\`\`\`
```

**Sybil will:**
1. Run `echo "test"` command
2. Compare output to `test`
3. Fail if output doesn't match

### File Verification

**For examples that create files:**

```markdown
<!-- verify-file: output.txt expected: expected-output.txt -->

\`\`\`console
$ {{ cookiecutter.command_name }} input.txt > output.txt
\`\`\`
```

**Sybil will:**
1. Run the command
2. Compare `output.txt` with `fixtures/expected-output.txt`
3. Delete `output.txt` after test

### Fixture Files

**Organize test data:**
```
docs/examples/fixtures/
├── input/
│   ├── sample.txt
│   └── complex-data.json
└── expected/
    ├── expected-output.txt
    └── expected-result.json
```

**Reference in examples:**
```markdown
\`\`\`console
$ {{ cookiecutter.command_name }} fixtures/input/sample.txt
Expected output here
\`\`\`
```

### Skipping Template Docs

**Mark work-in-progress docs:**

```markdown
# ⚠️ Template doc: Testing disabled ⚠️

This document is under development. Examples are not tested yet.

\`\`\`python
# This code won't be tested
incomplete_example()
\`\`\`
```

**Remove the warning when ready to enable testing.**

### Testing Documentation

```bash
# Test all documentation examples
pytest docs/

# Test specific document
pytest docs/getting-started/quick-start.md

# Run with verbose output
pytest docs/ -v

# Skip slow doc tests
pytest docs/ -m "not slow"
```

---

## Writing Guidelines

### Be Concise

- One idea per paragraph
- Short sentences
- Active voice
- Remove unnecessary words

**Bad:** "It should be noted that the program can be used to process files."
**Good:** "The program processes files."

### Show Don't Tell

**Bad:**
```markdown
The tool is very fast and efficient.
```

**Good:**
```markdown
The tool processes 1M lines/second:

\`\`\`console
$ time {{ cookiecutter.command_name }} large-file.txt
Processed 10000000 lines in 9.8s
\`\`\`
```

### Use Examples Liberally

**Every feature should have:**
1. Simple example (basic usage)
2. Real-world example (practical application)
3. Edge case example (handling unusual input)

### Code References

**Reference specific locations:**

```markdown
The validation logic is implemented in `src/{{ cookiecutter.project_slug }}/validator.py:45`
```

**Pattern:** `file_path:line_number`

**Benefits:**
- Users can navigate directly to code
- Easy to verify references are current
- Clear, unambiguous

---

## Documentation Review Checklist

Before completing documentation:

- [ ] All code examples tested (or doc marked with warning)
- [ ] Examples are practical and realistic
- [ ] No placeholder content ("TODO", "Coming soon")
- [ ] Cross-references are valid
- [ ] Spelling and grammar checked
- [ ] Renders correctly (`mkdocs serve`)
- [ ] Navigation makes sense
- [ ] Search finds relevant content

---

## Building and Previewing

### Local Preview

```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Serve documentation locally
mkdocs serve

# Opens at http://127.0.0.1:8000
```

### Build Documentation

```bash
# Build static site
mkdocs build

# Output in site/
```

### Documentation Testing

```bash
# Test all doc examples
pytest docs/

# Test and show coverage
pytest docs/ --cov=src/{{ cookiecutter.project_slug }}
```

---

## Common Documentation Patterns

### CLI Command Documentation

```markdown
## Command Name

Brief description.

### Usage

\`\`\`console
$ {{ cookiecutter.command_name }} [OPTIONS] FILE
\`\`\`

### Options

- `--option`: Description
- `-v, --verbose`: Enable verbose output

### Examples

Basic usage:
\`\`\`console
$ {{ cookiecutter.command_name }} input.txt
Output
\`\`\`

With options:
\`\`\`console
$ {{ cookiecutter.command_name }} --verbose input.txt
Detailed output
\`\`\`
```

### API Documentation

```markdown
## Function Name

\`\`\`python
def function_name(param: str) -> bool:
\`\`\`

Description of what it does.

**Parameters:**
- `param` (str): Description

**Returns:**
- bool: Description

**Example:**
\`\`\`python
from {{ cookiecutter.project_slug }} import function_name

result = function_name("value")
assert result is True
\`\`\`
```

---

## Next Steps

**Related guidance:**
- [Development](./development.md) - Code standards
- [Testing](./testing.md) - Test patterns
- [Workflows](./workflows/) - Common workflows

**Related documentation:**
- [IMPLEMENTATION.md](../dev-docs/design/IMPLEMENTATION.md) - Implementation details
- [TESTING_STRATEGY.md](../dev-docs/testing/TESTING_STRATEGY.md) - Test strategy
