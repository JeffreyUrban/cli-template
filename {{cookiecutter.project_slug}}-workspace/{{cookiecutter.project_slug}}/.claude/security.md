# Security Guidance

Security considerations and best practices for CLI applications.

**Inherits from:** [../CLAUDE.md](../CLAUDE.md) - Read universal rules first

---

## Philosophy

**Check for vulnerabilities** - Always review code for common security issues.

**Fix immediately** - If you notice insecure code, fix it immediately and document in commit.

---

## Security Checklist

Before committing code, check for:

- [ ] Command injection vulnerabilities
- [ ] SQL injection (use parameterized queries)
- [ ] XSS vulnerabilities
- [ ] Path traversal issues
- [ ] Secrets in code or version control
- [ ] OWASP Top 10 vulnerabilities

---

## Common Vulnerabilities

*Add specific security patterns and vulnerabilities discovered in this project*

### Command Injection

**Bad:**
\`\`\`python
import os
os.system(f"cat {user_input}")  # Dangerous!
\`\`\`

**Good:**
\`\`\`python
from pathlib import Path
Path(user_input).read_text()  # Safe, validates path
\`\`\`

### Path Traversal

**Bad:**
\`\`\`python
def read_file(filename):
    return open(filename).read()  # Can access any file!
\`\`\`

**Good:**
\`\`\`python
def read_file(filename):
    base = Path("/safe/directory")
    filepath = (base / filename).resolve()
    
    if not filepath.is_relative_to(base):
        raise ValueError("Invalid path")
    
    return filepath.read_text()
\`\`\`

---

## Secrets Management

**Never commit:**
- API keys
- Passwords
- Tokens
- Private keys
- .env files with secrets

**Use environment variables:**
\`\`\`python
import os
api_key = os.environ.get("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable required")
\`\`\`

**Add to .gitignore:**
\`\`\`
.env
*.key
secrets.json
credentials.json
\`\`\`

---

## Input Validation

*Add input validation patterns specific to this project*

**Validate user input:**
\`\`\`python
def process_input(user_input: str) -> str:
    # Validate
    if not user_input or len(user_input) > 1000:
        raise ValueError("Invalid input length")
    
    # Sanitize
    safe_input = user_input.strip()
    
    return process(safe_input)
\`\`\`

---

## Dependency Security

**Check for vulnerabilities:**
\`\`\`bash
# Using pip-audit
pip install pip-audit
pip-audit

# Or safety
pip install safety
safety check
\`\`\`

---

## Safe File Operations

*Add file operation security patterns*

**Check before operations:**
\`\`\`python
from pathlib import Path

def safe_write(filepath: Path, content: str):
    # Validate path
    if not filepath.parent.exists():
        raise ValueError("Parent directory doesn't exist")
    
    # Check permissions
    if filepath.exists() and not filepath.is_file():
        raise ValueError("Not a regular file")
    
    filepath.write_text(content)
\`\`\`

---

## Subprocess Security

**Use list form, not shell:**
\`\`\`python
import subprocess

# Bad
subprocess.run(f"ls {user_input}", shell=True)  # Command injection!

# Good
subprocess.run(["ls", user_input], shell=False)
\`\`\`

---

## Safe rm -rf Usage

**Never use wildcards in dangerous commands:**

\`\`\`bash
# NEVER do this
rm -rf *
rm -rf ~/*

# ALWAYS specify exact targets within project
rm -rf .venv
rm -rf specific-directory-name
rm -rf /tmp/my-temp-dir
\`\`\`

**Rules:**
- Never use `*` or `~` with `rm -rf`
- Never `rm -rf` outside project directory (except /tmp with specific subdirectory)
- Always specify exact target paths

---

## Next Steps

**Related guidance:**
- [Development](./development.md) - Input validation patterns
- [Testing](./testing.md) - Security testing
