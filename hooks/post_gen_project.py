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

    # For now, just keep the current LICENSE file
    # Users can manually update it for other licenses
    # (We could add all license files to the template later)

    print("\n" + "=" * 60)
    print(f"✨ Created project: {{ cookiecutter.project_name }}")
    print("=" * 60)
    print("\n📝 Next steps:")
    print(f"   1. cd {{ cookiecutter.project_slug }}")
    print("   2. git init")
    print("   3. uv venv && source .venv/bin/activate")
    print("   4. uv pip install -e '.[dev,docs]'")
    print("   5. pre-commit install")
    print("   6. pytest  # Verify everything works")
    print("\n📚 Documentation:")
    print("   - See README.md for usage instructions")
    print("   - See TEMPLATE.md for customization guide")
    print("   - Run 'mkdocs serve' to view docs locally")
    print("\n🔧 Customize:")
    print("   - Replace 'placeholder' placeholders with your content")
    print("   - Update docs/ with your examples")
    print("   - Add your implementation to src/{{ cookiecutter.project_slug }}/")
    print("\n" + "=" * 60)
    print()


if __name__ == "__main__":
    main()
