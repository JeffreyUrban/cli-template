# .claude/ Directory

This directory contains **scope-specific guidance** for Claude Code when working on this project.

## Purpose

The main `CLAUDE.md` at the project root provides universal rules and navigation. This directory contains detailed guidance organized by scope/concern.

## Structure

```
.claude/
├── README.md           # This file - explains the structure
├── development.md      # Coding standards, patterns, tools
├── testing.md          # Test strategy, pytest, coverage
├── documentation.md    # Doc standards, MkDocs, Sybil
├── workflows/          # Common task workflows
│   ├── feature-development.md
│   ├── bug-fixing.md
│   └── releasing.md
└── handoffs/           # Context preservation between instances
    └── README.md       # Handoff template and guidance
```

## When to Use Each File

**[development.md](./development.md)** - Use when:
- Writing or modifying code
- Making architectural decisions
- Choosing libraries or patterns
- Setting up development environment

**[testing.md](./testing.md)** - Use when:
- Writing or updating tests
- Debugging test failures
- Organizing test structure
- Setting coverage requirements

**[documentation.md](./documentation.md)** - Use when:
- Writing or updating docs
- Adding code examples to docs
- Organizing documentation structure
- Testing documentation examples

**[workflows/](./workflows/)** - Use when:
- Starting a common task (feature, bug fix, release)
- Need step-by-step checklist
- Ensuring consistency across tasks

**[handoffs/](./handoffs/)** - Use when:
- Transitioning work to another Claude instance
- End of session with incomplete work
- Blocking issue requires pause
- Need to preserve complex context

## Principles

1. **Inheritance:** All files inherit rules from main `CLAUDE.md`
2. **Specificity:** Each file focuses on its scope - no duplication
3. **Actionable:** Every file should answer "what should Claude do?"
4. **Examples:** Show don't tell - include code examples
5. **Links:** Reference authoritative sources (code, dev-docs) rather than duplicating

## Updating This Structure

**Add new scope file when:**
- A scope has >50 lines of guidance
- Multiple Claude instances work on the scope
- The scope has distinct patterns/standards

**Don't add new files for:**
- Temporary guidance (put in main CLAUDE.md with TODO)
- Single-task guidance (put in workflows/)
- Implementation details (put in dev-docs/)

## Maintenance

**When to update:**
- New patterns emerge → Update relevant scope file
- Standards change → Update scope file and main CLAUDE.md navigation
- Workflow improves → Update workflows/
- Universal rule → Update main CLAUDE.md only

**Version control:**
- Commit guidance changes with related code
- PRs should update guidance if they change patterns
- Review guidance during code review
