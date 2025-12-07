# settings.local.json Philosophy

## Purpose

The `.claude/settings.local.json` file pre-approves common commands so Claude Code can work efficiently without constantly asking for permission. The goal is to **eliminate friction** while maintaining reasonable safety boundaries.

## Philosophy

### Be Liberal, Not Conservative

**Optimize for developer productivity, not theoretical purity.**

- If Claude uses a command frequently (even if it "should" use a different tool), approve it
- If a tool is common in CLI development, approve it
- The cost of repeated permission prompts > risk of approved safe commands
- Don't enforce best practices through permissions - that's what guidance files are for

### Template vs Generated Project

**Template repo** (`cli-template`):
- `.claude/settings.local.json` is committed and distributed
- Contains minimal permissions needed for template maintenance
- Includes: cookiecutter, basic git, basic testing

**Generated projects** (from template):
- Start with comprehensive `settings.local.json` from template
- File gets gitignored during Initial Project Kickoff (step 6 in CLAUDE.md)
- Users customize freely without committing changes
- Pre-populated with everything likely needed for CLI development

## What to Include

### 1. **Project Context from Template Variables**
Use cookiecutter variables for project-specific commands:
```json
"Bash({{ cookiecutter.command_name }}:*)",
"Bash(NO_COLOR=1 {{ cookiecutter.command_name }}:*)",
"WebFetch(domain:{{ cookiecutter.project_slug }}.readthedocs.io)"
```

### 2. **Template Dependencies & Tools**
If the template includes it, approve related commands:
- Template uses typer/rich → approve their documentation domains
- Template uses pytest → approve all pytest variants
- Template has Homebrew tap → approve brew inspection (not install/uninstall)
- Template uses MkDocs → approve mkdocs commands and domain

### 3. **Common Development Tools**
Approve tools commonly used in CLI development:
- Shell: `sed`, `awk`, `echo`, `printf`, `grep`, `find`
- JSON/YAML: `jq`, `yamllint`
- Debugging: `xxd`, `hexdump`, `timeout`, `pkill`
- Version control: All common git commands, all gh (GitHub CLI) commands
- Testing: All pytest variants, coverage

### 4. **File Path Patterns**
Use wildcards for common patterns:
```json
"Bash(/tmp/*)",
"Bash(docs/**)",
"Bash(tests/**)",
"Bash(*.log)",
"Bash(expected-*)",
"Bash(output.*)"
```

### 5. **Environment Variables**
Approve common test/debug patterns:
```json
"Bash(CI=1 pytest:*)",
"Bash(NO_COLOR=1 *)",
"Bash(COLUMNS=* *)",
"Bash(SKIP=* pre-commit run:*)"
```

### 6. **Shell Constructs**
Claude uses these despite guidance to avoid - approve them:
```json
"Bash(echo:*)",
"Bash(printf:*)",
"Bash(for:*)",
"Bash(while read:*)",
"Bash(done)"
```

## What to Exclude/Deny

### Safety Boundaries

**Deny destructive operations:**
```json
"deny": [
  "Bash(brew install:*)",    // System modifications
  "Bash(brew uninstall:*)",
  "Bash(rm -rf:*)",          // Bulk deletion
  "Bash(sudo:*)"             // Privilege escalation
]
```

**Exclude localhost/development servers:**
```json
// Don't approve by default:
"WebFetch(domain:127.0.0.1)",
"WebFetch(domain:localhost)"
```

**Project-specific accumulated paths:**
Don't pre-approve hundreds of specific fixture files, output files, etc. These accumulate naturally as users work and approve them individually.

## Sources of Truth

When building settings.local.json for a new template/project, reference:
1. **This template's dependencies** - Check `pyproject.toml` for libraries
2. **Existing projects** - Look at settings from mature projects (uniqseq, patterndb-yaml)
3. **Common patterns** - Shell commands, git workflows, testing approaches
4. **Template structure** - Docs organization, test organization, scripts

## Maintenance

**For template repo (`cli-template`):**
- Keep minimal - only what's needed for template development
- Don't include project-specific stuff (that goes in generated projects)

**For generated projects:**
- Start comprehensive - include everything likely needed
- Users customize locally (file is gitignored)
- Accumulate project-specific permissions over time
- Don't commit back to template

## Example Workflow

When a new common tool/pattern emerges:
1. Notice repeated permission prompts across multiple projects
2. Identify if it's generally useful or project-specific
3. If general: Add to template's settings.local.json
4. If project-specific: User adds to their local settings (gitignored)
5. Template changes distribute to new projects only (existing projects don't auto-update)