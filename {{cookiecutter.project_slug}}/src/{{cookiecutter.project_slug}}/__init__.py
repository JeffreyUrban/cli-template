"""{{ cookiecutter.project_slug }} - placeholder."""

from .{{ cookiecutter.project_slug }} import {{ cookiecutter.class_name }}

# Version is managed by hatch-vcs and set during build
try:
    from ._version import __version__
except ImportError:
    # Fallback for development installs without build
    __version__ = "0.0.0.dev0+unknown"

__all__ = ["{{ cookiecutter.class_name }}", "__version__"]
