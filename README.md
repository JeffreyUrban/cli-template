# Python CLI Template

A production-ready, opinionated [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for modern Python CLI applications.

## ✨ What You Get

### Main Project
- 🎨 **Modern CLI framework**: typer + rich for beautiful terminal UIs
- ⚡️ **Fast package management**: uv for 10-100x faster installs
- 🧪 **Complete test suite**: pytest with organized markers (unit/integration/property)
- 📚 **Beautiful tested documentation**: MkDocs Material with live, tested code examples (Sybil)
- 🔍 **Code quality tools**: ruff (format + lint) + mypy (type checking)
- 🪝 **Git hooks**: pre-commit with automated checks
- 📦 **Modern packaging**: pyproject.toml + hatch-vcs for git-based versioning
- 🎯 **PyCharm ready**: Run configurations included
- ✅ **Fully working**: All 88 tests pass out of the box
- 🐙 **GitHub configuration script**: Automated repo settings (squash merge, branch protection)

### Homebrew Tap
- 🍺 **Automated Homebrew distribution**: Complete tap repository structure
- 🔄 **Auto-update workflows**: Formulas update automatically on PyPI release
- ✅ **CI/CD ready**: Brew test-bot integration for quality checks
- 📋 **Formula template**: Pre-configured with standard Python CLI dependencies

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- [cookiecutter](https://cookiecutter.readthedocs.io/): `pip install cookiecutter` or `brew install cookiecutter`

### Generate Your Project

```bash
cookiecutter gh:JeffreyUrban/cli-template
```

You'll be prompted for:

- **project_name**: "My Awesome CLI" (human-readable)
- **project_slug**: my-awesome-cli (auto-generated, uses hyphens for CLI/repo name)
- **project_short_description**: Brief description of your tool
- **author_name**: Your Name
- **author_email (optional)**: your.email@example.com
- **github_username**: yourusername
- **python_version**: 3.9 (minimum Python version)
- **license**: MIT, Apache-2.0, BSD-3-Clause, or GPL-3.0
- **command_name**: my-awesome-cli (CLI command, defaults to project_slug)

### Naming Convention

This template enforces hyphen-based naming for consistency with CLI best practices:

- **CLI command**: `my-awesome-cli` (hyphens)
- **Repository name**: `my-awesome-cli` (hyphens)
- **Directory name**: `my-awesome-cli` (hyphens)
- **Python package**: `my_awesome_cli` (underscores, auto-converted internally)

This follows the standard convention used by popular CLI tools like `docker-compose`, `git-flow`, and `gh-cli`.

### Example Session

```bash
$ cookiecutter gh:JeffreyUrban/cli-template
project_name [My CLI Tool]: Weather CLI
project_slug [weather-cli]:
project_short_description [A brief description of what your CLI tool does]: Get weather forecasts from the command line
author_name [Your Name]: Jane Developer
author_email [your.email@example.com]: jane@example.com
github_username [yourusername]: janedev
python_version [3.9]:
Select license:
1 - MIT
2 - Apache-2.0
3 - BSD-3-Clause
4 - GPL-3.0
Choose from 1, 2, 3, 4 [1]:
command_name [weather-cli]: weather

✨ Created project: Weather CLI

📦 Two repositories created:
   1. weather-cli/ - Main project
   2. homebrew-weather-cli/ - Homebrew tap
```

### Set Up Your New Project

The template creates a workspace directory containing two repositories:
- **weather-cli-workspace/weather-cli/** - Main project
- **weather-cli-workspace/homebrew-weather-cli/** - Homebrew tap

#### Main Project Setup

```bash
cd weather-cli-workspace/weather-cli

# Initialize git
git init

# Create virtual environment
uv venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows

# Install dependencies
uv pip install -e '.[dev,docs]'

# Set up git hooks
pre-commit install

# Verify everything works
pytest

# View documentation
mkdocs serve
```

#### GitHub Configuration (Optional)

After pushing your project to GitHub, configure repository settings with the included script:

```bash
# Install GitHub CLI if not already installed
brew install gh  # macOS/Linux
# or download from https://cli.github.com/

# Authenticate with GitHub
gh auth login

# Run configuration script
./scripts/configure-github.sh
```

This automatically configures:
- **All merge methods enabled** (merge commits, squash, rebase) with squash as default
- **Branch protection** on main (prevents force pushes, enforces rules for admins)
- **Auto-delete branches** after merge
- **Auto-merge** capability
- **Branch update suggestions** (prompts to update PRs when base branch changes)

See the [GitHub Configuration](#-github-repository-settings) section for details.

## 📁 What's Included

Your generated workspace will have:

```
your-project-workspace/
├── your-project/               # Main Python project
│   ├── src/
│   │   └── your_project/
│   │       ├── __init__.py
│   │       ├── cli.py          # CLI interface (typer + rich)
│   │       └── your_project.py # Core logic (placeholder)
│   ├── tests/
│   │   ├── fixtures/           # Test data
│   │   ├── test_*.py          # Organized tests
│   │   └── conftest.py        # Shared fixtures
│   ├── docs/                   # MkDocs documentation
│   │   ├── getting-started/
│   │   ├── features/
│   │   ├── use-cases/
│   │   ├── guides/
│   │   └── reference/
│   ├── scripts/                # Utility scripts
│   │   └── configure-github.sh # GitHub repo configuration
│   ├── .github/                # GitHub Actions (tests, publish, update-homebrew)
│   ├── .run/                   # PyCharm run configs
│   ├── pyproject.toml         # All config in one place
│   ├── mkdocs.yml             # Docs configuration
│   ├── .pre-commit-config.yaml # Git hooks
│   └── README.md              # Your project README
│
└── homebrew-your-project/      # Homebrew tap repository
    ├── Formula/
    │   └── your-project.rb    # Homebrew formula (with placeholders)
    ├── .github/workflows/
    │   ├── tests.yml          # Brew test-bot integration
    │   ├── publish.yml        # Auto-merge workflow
    │   └── update-formula.yml # Auto-update from PyPI
    ├── .gitignore
    ├── LICENSE
    └── README.md              # Homebrew tap instructions
```

## 🐙 GitHub Repository Settings

The template includes a script to automatically configure your GitHub repository with recommended settings for professional project management.

### What Gets Configured

**Merge Strategy:**
- All merge methods enabled (merge commits, squash, rebase) for maximum flexibility
- Squash merge set as default (keeps history clean with one commit per PR)
- Squash commit title uses PR title, message includes all commits

**Branch Protection on `main`:**
- Prevents force pushes and branch deletion
- Enforces rules for administrators
- Ready for required status checks (add after setting up CI/CD)

**Pull Request Settings:**
- Auto-delete branches after merge (keeps repo clean)
- Auto-merge enabled (allows PRs to merge when checks pass)
- Branch update suggestions enabled (prompts to update when base branch changes)

### Usage

```bash
# The script auto-detects your repository from git remote
./scripts/configure-github.sh

# Or specify manually
./scripts/configure-github.sh your-username/your-repo
```

**Requirements:**
- [GitHub CLI](https://cli.github.com/) installed and authenticated
- Admin permissions on the repository

### Adding Status Checks

After setting up GitHub Actions, add required status checks to ensure tests pass before merging:

```bash
gh api -X PATCH repos/your-username/your-repo/branches/main/protection/required_status_checks \
  -F strict=false \
  -f 'contexts[]=quality' \
  -f 'contexts[]=link-check' \
  -f 'contexts[]=test (3.9)' \
  -f 'contexts[]=test (3.10)' \
  -f 'contexts[]=test (3.11)' \
  -f 'contexts[]=test (3.12)' \
  -f 'contexts[]=test (3.13)' \
  -f 'contexts[]=test (3.14)' \
  -f 'contexts[]=docs/readthedocs.org:your-project'
```

**Notes:**
- Use `-F` (uppercase) for `strict` to send it as a boolean, not a string
- The single quotes around each `-f` parameter are required for zsh (macOS default shell) to prevent glob expansion
- This matches the workflow pattern where `quality` and `link-check` run in parallel, followed by matrix tests

The configuration script outputs these commands customized for your project at the end of execution.

## 🎯 Features

### Modern Python Stack

- **typer**: Type-based CLI framework with automatic help
- **rich**: Beautiful terminal output (tables, progress bars, colors)
- **pytest**: Modern testing with fixtures and markers
- **ruff**: All-in-one linter/formatter (replaces black, flake8, isort, etc.)
- **mypy**: Static type checking
- **uv**: Lightning-fast package installer

### Production-Ready Testing

- Organized test markers: `@pytest.mark.unit`, `@pytest.mark.integration`, `@pytest.mark.property`
- Example fixtures and test patterns
- Sybil integration for testing documentation examples
- 88 passing tests included as examples

### Beautiful Documentation

- MkDocs Material theme
- Live code examples that are tested
- Organized sections: Getting Started, Features, Guides, Reference
- GitHub Pages ready
- ReadTheDocs compatible

### Developer Experience

- Pre-commit hooks for code quality
- PyCharm run configurations
- GitHub Actions workflow structure
- Automatic versioning from git tags

### Homebrew Distribution

- **Complete tap structure**: Ready-to-use Homebrew tap repository
- **Automated formula updates**: Workflows trigger on PyPI release
- **Quality assurance**: Brew test-bot integration for CI/CD
- **Standard dependencies**: Pre-configured with typer, rich, and transitive deps
- **Easy setup**: Detailed instructions in HOMEBREW_AUTOMATION_SETUP.md

## 🛠️ Customization

After generating your project:

1. **Replace "placeholder" placeholders** - These are intentional markers for you to replace
2. **Implement your logic** in `src/your_project/your_project.py`
3. **Update CLI options** in `src/your_project/cli.py`
4. **Add your documentation** in `docs/`
5. **Update test fixtures** in `tests/fixtures/`

See the generated `TEMPLATE.md` in your project for detailed customization guide.

## 📖 Documentation

The template includes comprehensive documentation:

- **README.md** (in generated project): Project overview and installation
- **TEMPLATE.md** (in generated project): Detailed customization guide
- **CLAUDE.md** (in generated project): AI coding assistant guidelines
- **docs/**: Full MkDocs documentation site

## 🤝 Why This Template?

### Opinionated Choices

This template makes specific technology choices to provide the best modern Python CLI development experience:

- **Hyphen-based naming**: CLI commands and repos use hyphens (like `docker-compose`, `git-flow`)
- **typer over click/argparse**: Type-safe, less boilerplate
- **rich for output**: Beautiful terminal UIs out of the box
- **ruff over black+flake8**: Single tool, 10-100x faster
- **uv over pip**: 10-100x faster, reliable
- **pytest over unittest**: More concise, better fixtures
- **MkDocs Material**: Beautiful docs with minimal config

### Production-Ready

- All tests pass immediately
- Documentation builds without errors
- Pre-commit hooks configured
- Type hints throughout
- Follows modern Python packaging standards (PEP 517/518/621)

## 📦 Examples of Projects Using This Template

[uniqseq](https://github.com/JeffreyUrban/uniqseq)

## 🐛 Issues & Contributions

Found a bug or want to improve the template?

- **Issues**: [github.com/JeffreyUrban/cli-template/issues](https://github.com/JeffreyUrban/cli-template/issues)
- **Pull Requests**: Welcome!

## 📄 License

This template is MIT licensed. Generated projects can use any license you choose during generation.

## 🙏 Acknowledgments

Built with:
- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [typer](https://typer.tiangolo.com/)
- [rich](https://rich.readthedocs.io/)
- [pytest](https://pytest.org/)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [ruff](https://docs.astral.sh/ruff/)
- [uv](https://docs.astral.sh/uv/)
- [Homebrew](https://brew.sh/)
- [Sybil](https://sybil.readthedocs.io)
