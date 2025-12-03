# CLAUDE.md

Guidance for Claude Code (claude.ai/code) when working with this repository.

## Overview

This file is the **entry point** for Claude guidance. Detailed guidance is organized by scope in the `.claude/` directory.

**Philosophy:** Keep this file focused on universal rules and navigation. Put detailed, scope-specific guidance in dedicated files.

## Critical Rules

**NEVER mention version numbers** (v0.x, v1.x, etc.) unless they have been explicitly agreed upon and documented in planning. Use:
- **"Stage X"** for implementation phases (e.g., "Stage 3: Pattern Libraries")
- **"Current implementation"** for what exists now
- **"Planned features"** or **"Future features"** for what's coming
- **"Milestone"** for completed work

**DO NOT** add version numbers to:
- Documentation
- Code comments
- Commit messages
- Planning documents
- Unless the user has explicitly specified and approved a versioning scheme and specific versions

**Safe rm -rf usage:**
- Never `rm -rf` with `*` or `~` in the target
- Never `rm -rf` outside of the project or /tmp
- Always specify specific targets within the project for `rm -rf`

## Project-Specific Critical Rules

**CRITICAL: Implement requirements correctly, don't document violations as limitations!**
- When given a requirement (e.g., "keep the most recent value"), implement it correctly
- Do NOT implement the opposite behavior and add a TODO noting it should be fixed later
- If the requirement needs clarification or would require significant changes, ASK first

**CRITICAL: Use proper solutions, not workarounds!**
- When encountering issues (especially in CI/testing), investigate the root cause
- Find the standard/best-practice solution for the problem
- Examples of workarounds to AVOID:
  - Weakening test assertions to pass (e.g., changing "window-size" to "window")
  - Adding `# type: ignore` comments instead of fixing type issues
  - Disabling linters/checkers instead of fixing the underlying issue
- Examples of proper solutions:
  - Setting environment variables for consistent behavior (e.g., `COLUMNS` for terminal width)
  - Using appropriate imports for Python version compatibility (e.g., `Optional` vs `|`)
  - Configuring tools correctly in config files
- If unsure whether a solution is a workaround or proper fix, ASK the user

**Evidence-Based Documentation:**
- Distinguish between **observed facts** and **inferred causes**
- Use precise language: "observed", "measured", "specified by user" vs "causes", "due to", "because"
- When debugging, document what was tried and what was observed, not assumed root causes
- If stating a cause, cite the evidence or mark as hypothesis

**When Asked to Justify Decisions:**
- If the user asks why you made a decision or assumption, search documentation and code comments for supporting evidence
- Present the evidence with specific references (file paths and line numbers where applicable)
- If no supporting evidence is found, acknowledge the assumption and ask for clarification
- Example: "I assumed X based on the comment at normalization_engine.py:117 which states '...'"

## Navigation

### Scope-Specific Guidance

Claude guidance is organized by scope:

- **[Development](.claude/development.md)** - Coding standards, patterns, tools, modern practices
- **[Testing](.claude/testing.md)** - Test strategy, pytest, coverage, oracle testing
- **[Documentation](.claude/documentation.md)** - Doc standards, MkDocs, Sybil, doc testing
- **[Workflows](.claude/workflows/)** - Common task workflows and checklists
- **[Handoffs](.claude/handoffs/)** - Context preservation between Claude instances

### Project Documentation

Key documentation by purpose:

**User Documentation:**
- **[README.md](./README.md)** - Project overview and installation

**Design Documentation:**
- **[dev-docs/design/IMPLEMENTATION.md](./dev-docs/design/IMPLEMENTATION.md)** - Implementation overview and design decisions
- **[dev-docs/design/ALGORITHM_DESIGN.md](./dev-docs/design/ALGORITHM_DESIGN.md)** - Detailed algorithm design
- **[dev-docs/design/DESIGN_RATIONALE.md](./dev-docs/design/DESIGN_RATIONALE.md)** - Design rationale and trade-offs

**Planning Documentation:**
- **[dev-docs/planning/PLANNING.md](./dev-docs/planning/PLANNING.md)** - Roadmap and feature planning

**Testing Documentation:**
- **[dev-docs/testing/TESTING_STRATEGY.md](./dev-docs/testing/TESTING_STRATEGY.md)** - Test strategy and organization
- **[dev-docs/testing/TEST_COVERAGE.md](./dev-docs/testing/TEST_COVERAGE.md)** - Test coverage plan
- **[dev-docs/testing/ORACLE_TESTING.md](./dev-docs/testing/ORACLE_TESTING.md)** - Oracle-based testing approach

## Project Context

**Tech Stack:**
- **Language:** Python {{ cookiecutter.python_version }}+
- **CLI Framework:** typer + rich
- **Testing:** pytest with organized markers
- **Documentation:** MkDocs Material with Sybil (tested code examples)
- **Code Quality:** ruff (lint + format) + mypy (type checking)
- **Package Management:** uv for fast installs
- **Version Control:** Git with conventional commits

**Project Structure:**
- `src/{{ cookiecutter.project_slug }}/` - Source code
- `tests/` - Test files with pytest markers
- `docs/` - MkDocs documentation with tested examples
- `dev-docs/` - Design and planning documentation
- `.claude/` - Claude guidance files (this system)

**Current Date & Version Awareness:**
- **IMPORTANT:** Always check the current date in the system `<env>` tag
- When searching or making decisions based on versions/dates, use the current date from `<env>`, NOT historical information
- Python 3.13 was released in October 2024
- Python 3.14 was released in October 2025 (per devguide.python.org/versions/)

## Universal Workflows

### Git & Commits

**Session Start:**
- Always `git pull` when starting work on a project with a git repository
- Ensures you're working with the latest code, especially when multiple people or Claude instances work on the project

**Remote Configuration:**
- Use SSH for GitHub remotes, not HTTPS
- Check: `git remote -v`
- Switch if needed: `git remote set-url origin git@github.com:username/repo.git`

**Only create commits when requested by the user.** If unclear, ask first.

When creating commits:
- Follow conventional commit format
- Include co-authorship footer:
  ```
  🤖 Generated with [Claude Code](https://claude.com/claude-code)

  Co-Authored-By: Claude <noreply@anthropic.com>
  ```
- See detailed commit workflow in system instructions

### Tool Usage

- **Proactively use Task tool** with specialized agents when the task matches the agent's description
- **Use dedicated tools** instead of bash for file operations (Read/Edit/Write, not cat/sed)
- **Run tools in parallel** when they're independent (multiple reads, searches, etc.)
- See [Development](.claude/development.md) for tool-specific guidance

### Communication

- **Be concise** - CLI output is displayed in terminal
- **Use markdown** - GitHub-flavored markdown for formatting
- **Avoid emojis** unless explicitly requested
- **Output text directly** - never use bash echo or comments to communicate
- **Don't be markety** - Avoid promotional language, "New!" callouts, or marketing-style announcements

## Handoffs Between Claude Instances

**When transitioning work to another Claude instance:**

1. **Create handoff document** in `.claude/handoffs/YYYY-MM-DD-topic.md`
2. **Document state**: What's complete, in progress, blocked
3. **List decisions**: Key technical decisions and rationale
4. **Note open questions**: Ambiguities or needed clarifications
5. **Provide commands**: How to resume work

See [Handoffs README](.claude/handoffs/README.md) for detailed template and guidance.

**When to create handoffs:**
- Switching Claude instances mid-task
- End of session with incomplete work
- Blocked by external dependency
- Complex feature requiring context preservation

## Maintenance Rules

**When code works correctly:**
- Remove outdated code and documentation
- Update relevant documentation
- Add test cases for issues found and fixed

**Before creating directory structures:**
- Discuss scope and organization with user
- Don't create documentation/planning hierarchies without approval

## Getting Started

1. **Review this CLAUDE.md** for universal rules and navigation
2. **Check scope-specific guidance** in `.claude/` for your current task:
   - Adding features? → [Development](.claude/development.md)
   - Writing tests? → [Testing](.claude/testing.md)
   - Updating docs? → [Documentation](.claude/documentation.md)
3. **Reference project documentation** in `dev-docs/` for design decisions
4. **Follow workflows** in `.claude/workflows/` for common tasks

## About This Structure

**Why split CLAUDE.md?**
- Main file stays focused and navigable
- Scope-specific details don't clutter universal rules
- Different Claude instances can focus on relevant guidance
- Easier to maintain and update

**When to update:**
- **This file:** Universal rules, navigation, project context
- **`.claude/*.md`:** Scope-specific patterns, standards, examples
- **`dev-docs/`:** Design decisions, architecture, rationale
- **`docs/`:** User-facing documentation

**File organization principle:**
- `CLAUDE.md` - Project-wide rules, entry point (this file)
- `.claude/*.md` - Specialized guidance by scope
- `dev-docs/**/*.md` - Design decisions, architecture
- `docs/**/*.md` - User-facing documentation

**Never** put implementation details in CLAUDE.md files - link to dev-docs or code instead.
