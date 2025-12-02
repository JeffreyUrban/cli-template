# Homebrew Tap for {{ cookiecutter.project_slug }}

This is the official Homebrew tap for [{{ cookiecutter.project_slug }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}), {{ cookiecutter.project_short_description }}.

## Installation

### Quick Install

```bash
brew tap {{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
brew install {{ cookiecutter.command_name }}
```

### One-Line Install

```bash
brew install {{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/{{ cookiecutter.command_name }}
```

## What Gets Installed

When you install `{{ cookiecutter.command_name }}` via Homebrew, you get:

- ✅ **{{ cookiecutter.command_name }}** - {{ cookiecutter.project_short_description }}
- ✅ **Python dependencies** - All Python packages in an isolated virtualenv

## Features

- **Isolated environment** - Python packages don't conflict with your system Python
- **Easy updates** - `brew upgrade {{ cookiecutter.command_name }}` to get the latest version
- **Automatic formula updates** - New releases are published automatically

## Usage

After installation, the `{{ cookiecutter.command_name }}` command is available in your PATH:

```bash
# Check version
{{ cookiecutter.command_name }} --version

# Get help
{{ cookiecutter.command_name }} --help
```

## Updating

```bash
# Update Homebrew
brew update

# Upgrade {{ cookiecutter.command_name }}
brew upgrade {{ cookiecutter.command_name }}
```

## Uninstalling

```bash
# Remove {{ cookiecutter.command_name }}
brew uninstall {{ cookiecutter.command_name }}

# Remove the tap
brew untap {{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
```

## Documentation

- **Main Project**: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
- **PyPI**: https://pypi.org/project/{{ cookiecutter.package_name }}/

## Requirements

- **macOS** 11.0+ (Big Sur) or **Linux**
- **Python** {{ cookiecutter.python_version }}+ (provided by Homebrew)

## Troubleshooting

### Command not found after installation

```bash
# Ensure Homebrew's bin is in your PATH
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Check installation

```bash
# Verify {{ cookiecutter.command_name }} is installed
brew list {{ cookiecutter.command_name }}

# Test basic functionality
{{ cookiecutter.command_name }} --version
```

### Reinstall

```bash
brew reinstall {{ cookiecutter.command_name }}
```

## Development

This tap uses automated workflows to update the formula when new versions are released:

1. A new release is created in the main repository
2. The release workflow triggers this repository via `repository_dispatch`
3. The update workflow waits for the PyPI release
4. A pull request is automatically created with the updated formula
5. After review, the PR is merged to publish the update

For more details, see [`.github/workflows/update-formula.yml`](.github/workflows/update-formula.yml).

## Contributing

Issues and pull requests should be submitted to the main repository:
https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues

Formula-specific issues can be reported here:
https://github.com/{{ cookiecutter.github_username }}/homebrew-{{ cookiecutter.project_slug }}/issues

## License

The formula in this repository is licensed under the MIT License.

The {{ cookiecutter.project_slug }} software itself is also MIT licensed. See the [main repository](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}) for details.
