#!/usr/bin/env python
"""Post-generation hook for cookiecutter template."""

import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def remove_file(filepath: Path) -> None:
    """Remove a file if it exists."""
    if filepath.exists():
        filepath.unlink()


def main() -> None:
    """Execute post-generation tasks."""

    # Handle license files based on selection
    license_choice = "{{ cookiecutter.license }}"

    # License file mapping
    license_files = {
        "MIT": "LICENSE",
        "Apache-2.0": "LICENSE-APACHE",
        "BSD-3-Clause": "LICENSE-BSD",
        "GPL-3.0": "LICENSE-GPL",
    }

    # Remove LICENSE files if "None" is selected
    if license_choice == "None":
        # Remove LICENSE from main project
        main_license = PROJECT_DIRECTORY / "{{ cookiecutter.project_slug }}" / "LICENSE"
        remove_file(main_license)

        # Remove LICENSE from homebrew tap
        homebrew_license = PROJECT_DIRECTORY / "homebrew-{{ cookiecutter.project_slug }}" / "LICENSE"
        remove_file(homebrew_license)

    # For now, just keep the current LICENSE file for other license types
    # Users can manually update it for other licenses
    # (We could add all license files to the template later)

    print("\n" + "=" * 70)
    print(f"✨ Created project: {{ cookiecutter.project_name }}")
    print("=" * 70)
    print("\n📦 Two repositories created:")
    print(f"   1. {{ cookiecutter.project_slug }}/ - Main project")
    print(f"   2. homebrew-{{ cookiecutter.project_slug }}/ - Homebrew tap")
    print("\n📝 Main project setup ({{ cookiecutter.project_slug }}):")
    print(f"   1. cd {{ cookiecutter.project_slug }}-workspace/{{ cookiecutter.command_name }}")
    print("   2. git init")
    print("   3. uv venv && source .venv/bin/activate")
    print("   4. uv pip install -e '.[dev,docs]'")
    print("   5. pre-commit install")
    print("   6. pytest  # Verify everything works")
    print('   7. Prompt Claude Code: "Please perform Initial Project Kickoff"')
    print("   8. git add . && git commit -m 'Initial commit'")
    print(f"   9. Create GitHub repo: {{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}")
    print("   10. git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git")
    print("   11. git push -u origin main")
    print("\n🍺 Homebrew tap setup (homebrew-{{ cookiecutter.project_slug }}):")
    print(f"   1. cd ../homebrew-{{ cookiecutter.project_slug }}")
    print("   2. git init")
    print("   3. git add . && git commit -m 'Initial commit'")
    print(f"   4. Create GitHub repo: {{ cookiecutter.github_username }}/homebrew-{{ cookiecutter.project_slug }}")
    print("   5. git remote add origin git@github.com:{{ cookiecutter.github_username }}/homebrew-{{ cookiecutter.project_slug }}.git")
    print("   6. git push -u origin main")
    print("\n🔑 Required GitHub secrets (in main repo):")
    print("   - HOMEBREW_UPDATE_TOKEN: Personal access token with 'repo' scope")
    print("   - See HOMEBREW_AUTOMATION_SETUP.md for detailed setup")
    print("\n⚠️  Formula dependencies:")
    print("   - The Formula file has placeholder URLs and SHA256 hashes")
    print("   - After your first PyPI release, run the update-formula workflow")
    print("   - It will automatically populate the correct values")
    print("\n📚 Documentation:")
    print("   - See README.md for usage instructions")
    print("   - See HOMEBREW_AUTOMATION_SETUP.md for Homebrew setup")
    print("   - Run 'mkdocs serve' to view docs locally")
    print("\n🔧 Customize:")
    print("   - Replace 'placeholder' placeholders with your content")
    print("   - Update docs/ with your examples")
    print("   - Add your implementation to src/{{ cookiecutter.project_slug }}/")
    print("\n" + "=" * 70)
    print()


if __name__ == "__main__":
    main()
