# {{ cookiecutter.project_name }}

## ⚠️ Early Development - Not Ready for Use

**This project is under active development and is not ready for production use.**

- APIs may change without notice
- Documentation is incomplete
- No releases published yet
- Not accepting contributions at this time

> - **Star/watch the repo to be notified when the first release is available.**

**{{ cookiecutter.project_short_description }}**

[![PyPI version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![Python {{ cookiecutter.python_version }}+](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}+-blue.svg)](https://www.python.org/downloads/)
[![Documentation](https://img.shields.io/readthedocs/{{ cookiecutter.project_slug }})](https://{{ cookiecutter.project_slug }}.readthedocs.io/)
[![License: {{ cookiecutter.license }}](https://img.shields.io/badge/License-{{ cookiecutter.license }}-yellow.svg)](https://opensource.org/licenses/{{ cookiecutter.license }})

## Installation

### Via Homebrew (macOS/Linux)

```bash
brew tap {{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }} && brew install {{ cookiecutter.command_name }}
```

Homebrew manages the Python dependency and provides easy updates via `brew upgrade`.

### Via pipx (Cross-platform)

```bash
pipx install {{ cookiecutter.project_slug }}
```

[pipx](https://pipx.pypa.io/) installs in an isolated environment with global CLI access. Works on macOS, Linux, and Windows. Update with `pipx upgrade {{ cookiecutter.project_slug }}`.

### Via pip

```bash
pip install {{ cookiecutter.project_slug }}
```

Use `pip` if you want to use {{ cookiecutter.command_name }} as a library in your Python projects.

### From Source

```bash
# Development installation
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.command_name }}
cd {{ cookiecutter.command_name }}-workspace/{{ cookiecutter.command_name }}
pip install -e ".[dev]"
```

**Requirements:** Python PYTHON_VERSION_MIN_KICKOFF+

**IDE Configuration:**
- **PyCharm**: Project settings are pre-configured in `.idea/` (source roots automatically set)
- **VS Code**: Settings are pre-configured in `.vscode/settings.json` (includes pytest, ruff, pyright configuration)

## Quick Start

### Command Line

```bash
{{ cookiecutter.command_name }}
```

### Python API

```python
from {{ cookiecutter.project_slug }} import {{ cookiecutter.class_name }}

# Initialize with configuration
TEMPLATE_PLACEHOLDER = {{ cookiecutter.class_name }}(
    TEMPLATE_PLACEHOLDER=TEMPLATE_PLACEHOLDER
)

# Process stream
with open("app.log") as infile, open("clean.log", "w") as outfile:
    for line in infile:
        TEMPLATE_PLACEHOLDER.TEMPLATE_PLACEHOLDER(TEMPLATE_PLACEHOLDER, outfile)
    TEMPLATE_PLACEHOLDER.flush(outfile)
```

## Use Cases

- **TEMPLATE_PLACEHOLDER** - TEMPLATE_PLACEHOLDER

## How It Works

`{{ cookiecutter.command_name }}` uses TEMPLATE_PLACEHOLDER:

1. **TEMPLATE_PLACEHOLDER** - TEMPLATE_PLACEHOLDER

TEMPLATE_PLACEHOLDER.

## Documentation

**[Read the full documentation at {{ cookiecutter.project_slug }}.readthedocs.io](https://{{ cookiecutter.project_slug }}.readthedocs.io/)**

Key sections:
- **Getting Started** - Installation and quick start guide
- **Use Cases** - Real-world examples across different domains
- **Guides** - TEMPLATE_PLACEHOLDER selection, performance tips, common patterns
- **Reference** - Complete CLI and Python API documentation

## Development

```bash
# Clone repository
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.command_name }}.git
cd {{ cookiecutter.command_name }}-workspace/{{ cookiecutter.command_name }}

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov={{ cookiecutter.command_name }} --cov-report=html
```

### GitHub Repository Configuration

After creating your GitHub repository, run the configuration script to set up recommended settings:

```bash
./scripts/configure-github.sh
```

This script configures:
- **Merge strategy:** Squash and merge only (with other methods disabled)
- **Branch protection on main:**
  - Prevents force pushes and branch deletion
  - Enforces rules for administrators
  - Allows configuration of required status checks
- **Auto-delete branches** after merge
- **Auto-merge** capability

**Requirements:**
- [GitHub CLI](https://cli.github.com/) installed and authenticated (`gh auth login`)
- Admin permissions on the repository

The script will automatically detect your repository from the git remote, or you can specify it manually:

```bash
./scripts/configure-github.sh owner/repository-name
```

**Note:** After setting up GitHub Actions workflows, add required status checks by following the instructions shown at the end of the script output.

## Performance

- **Time complexity:** O(TEMPLATE_PLACEHOLDER)
- **Space complexity:** O(TEMPLATE_PLACEHOLDER)
- **Throughput:** TEMPLATE_PLACEHOLDER
- **Memory:** TEMPLATE_PLACEHOLDER

## License

MIT License - See [LICENSE](LICENSE) file for details

## Author

{{ cookiecutter.author_name }}{% if cookiecutter.author_email and cookiecutter.author_email != "(optional)" %} ({{ cookiecutter.author_email }}){% endif %}

---

**[Star on GitHub](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.command_name }})** | **[Report Issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.command_name }}/issues)**
