# ⚠️ Template doc: Testing disabled ⚠️

# Installation

`{{ cookiecutter.command_name }}` can be installed via Homebrew, pipx, pip, or from source.

## Requirements

- **Python PYTHON_VERSION_MIN_KICKOFF or higher** (for pip/pipx installations)
- **Homebrew** (for macOS/Linux Homebrew installation)

`{{ cookiecutter.command_name }}` works on Linux, macOS, and Windows.

## Via Homebrew (macOS/Linux)

```bash
brew tap jeffreyurban/{{ cookiecutter.command_name }}
brew install {{ cookiecutter.command_name }}
```

Homebrew manages the Python dependency and provides easy updates via `brew upgrade`.

## Via pipx (Cross-platform)

```bash
pipx install {{ cookiecutter.command_name }}
```

[pipx](https://pipx.pypa.io/) installs in an isolated environment with global CLI access. Works on macOS, Linux, and Windows. Update with `pipx upgrade {{ cookiecutter.command_name }}`.

## Via pip

```bash
pip install {{ cookiecutter.command_name }}
```

Use `pip` if you want to use {{ cookiecutter.command_name }} as a library in your Python projects.

## Via Source

For development or the latest unreleased features:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.command_name }}.git
cd {{ cookiecutter.command_name }}
pip install .
```

This installs `{{ cookiecutter.command_name }}` and its dependencies:

- **typer** - CLI framework
- **rich** - Terminal formatting and progress display

## Development Installation

For contributing or modifying `{{ cookiecutter.command_name }}`, install in editable mode with development dependencies:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.command_name }}.git
cd {{ cookiecutter.command_name }}
pip install -e ".[dev]"
```

Development dependencies include:

- **pytest** - Test framework
- **pytest-cov** - Code coverage
- **ruff** - Linting and formatting
- **pyright** - Type checking
- **pre-commit** - Git hooks for code quality

## Platform-Specific Notes

### Linux

Recommended installation methods:

- **Homebrew**: `brew tap jeffreyurban/{{ cookiecutter.command_name }} && brew install {{ cookiecutter.command_name }}`
- **pipx**: `pipx install {{ cookiecutter.command_name }}`
- **pip**: `pip install {{ cookiecutter.command_name }}`

!!! tip "Virtual Environments"
    If using pip directly, consider using a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install {{ cookiecutter.command_name }}
    ```

### macOS

Recommended installation methods:

- **Homebrew**: `brew tap jeffreyurban/{{ cookiecutter.command_name }} && brew install {{ cookiecutter.command_name }}` (recommended)
- **pipx**: `pipx install {{ cookiecutter.command_name }}`
- **pip**: `pip install {{ cookiecutter.command_name }}`

### Windows

Recommended installation methods:

- **pipx**: `pipx install {{ cookiecutter.command_name }}` (recommended)
- **pip**: `pip install {{ cookiecutter.command_name }}`

The `{{ cookiecutter.command_name }}` command will be available in your terminal after installation.

## Verify Installation

After installation, verify `{{ cookiecutter.command_name }}` is working:

```bash
{{ cookiecutter.command_name }} --version
{{ cookiecutter.command_name }} --help
```

Try a quick test:

```bash
echo -e "TEMPLATE_PLACEHOLDER" | {{ cookiecutter.command_name }} --TEMPLATE_PLACEHOLDER
```

Expected output:
```
TEMPLATE_PLACEHOLDER
```

## Upgrading

### Homebrew

```bash
brew upgrade {{ cookiecutter.command_name }}
```

### pipx

```bash
pipx upgrade {{ cookiecutter.command_name }}
```

### pip

```bash
pip install --upgrade {{ cookiecutter.command_name }}
```

### Source Installation

```bash
cd {{ cookiecutter.command_name }}
git pull
pip install --upgrade .
```

For development installations:

```bash
cd {{ cookiecutter.command_name }}
git pull
pip install --upgrade -e ".[dev]"
```

## Uninstalling

### Homebrew

```bash
brew uninstall {{ cookiecutter.command_name }}
```

### pipx

```bash
pipx uninstall {{ cookiecutter.command_name }}
```

### pip

```bash
pip uninstall {{ cookiecutter.command_name }}
```

## Troubleshooting

### Command Not Found

If `{{ cookiecutter.command_name }}` command is not found after installation:

1. **Check pip installed in the right location:**
   ```bash
   pip show {{ cookiecutter.command_name }}
   ```

2. **Verify Python scripts directory is in PATH:**
   ```bash
   python -m site --user-base
   ```
   Add `<user-base>/bin` to your PATH if needed.

3. **Use Python module syntax:**
   ```bash
   python -m {{ cookiecutter.command_name }} --help
   ```

### Import Errors

If you see import errors, ensure dependencies are installed:

```bash
pip install typer rich
```

Or reinstall with dependencies:

```bash
pip install --force-reinstall .
```

### Permission Errors

If you encounter permission errors, install for your user only:

```bash
pip install --user .
```

Or use a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install .
```

## Next Steps

- [Quick Start Guide](quick-start.md) - Learn basic usage
- [Basic Concepts](basic-concepts.md) - Understand how `{{ cookiecutter.command_name }}` works
- [CLI Reference](../reference/cli.md) - Complete command-line options
