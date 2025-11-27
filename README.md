# Python CLI Template

A production-ready, opinionated [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for modern Python CLI applications.

## ✨ What You Get

- 🎨 **Modern CLI framework**: typer + rich for beautiful terminal UIs
- ⚡️ **Fast package management**: uv for 10-100x faster installs
- 🧪 **Complete test suite**: pytest with organized markers (unit/integration/property)
- 📚 **Beautiful documentation**: MkDocs Material with live code examples (Sybil)
- 🔍 **Code quality tools**: ruff (format + lint) + mypy (type checking)
- 🪝 **Git hooks**: pre-commit with automated checks
- 📦 **Modern packaging**: pyproject.toml + hatch-vcs for git-based versioning
- 🎯 **PyCharm ready**: Run configurations included
- ✅ **Fully working**: All 88 tests pass out of the box

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
- **project_slug**: my_awesome_cli (auto-generated, Python package name)
- **project_short_description**: Brief description of your tool
- **author_name**: Your Name
- **author_email**: your.email@example.com
- **github_username**: yourusername
- **python_version**: 3.9 (minimum Python version)
- **license**: MIT, Apache-2.0, BSD-3-Clause, or GPL-3.0
- **command_name**: my_awesome_cli (CLI command, defaults to project_slug)

### Example Session

```bash
$ cookiecutter gh:JeffreyUrban/cli-template
project_name [My CLI Tool]: Weather CLI
project_slug [weather_cli]:
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
command_name [weather_cli]: weather

✨ Created project: Weather CLI
```

### Set Up Your New Project

```bash
cd weather_cli

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

## 📁 What's Included

Your generated project will have:

```
your-project/
├── src/
│   └── your_project/
│       ├── __init__.py
│       ├── cli.py              # CLI interface (typer + rich)
│       └── your_project.py     # Core logic (placeholder)
├── tests/
│   ├── fixtures/               # Test data
│   ├── test_*.py              # Organized tests
│   └── conftest.py            # Shared fixtures
├── docs/                       # MkDocs documentation
│   ├── getting-started/
│   ├── features/
│   ├── use-cases/
│   ├── guides/
│   └── reference/
├── .github/                    # GitHub Actions ready
├── .run/                       # PyCharm run configs
├── pyproject.toml             # All config in one place
├── mkdocs.yml                 # Docs configuration
├── .pre-commit-config.yaml    # Git hooks
└── README.md                  # Your project README
```

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
