"""Command-line interface for {{ cookiecutter.project_slug }}."""

import json
import re
import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import BinaryIO, Callable, Optional, TextIO, Union

import typer
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
)
from rich.table import Table

from . import __version__
from .{{ cookiecutter.project_slug }} import (
    {{ cookiecutter.class_name }},
)

app = typer.Typer(
    name="{{ cookiecutter.command_name }}",
    help="placeholder",
    context_settings={"help_option_names": ["-h", "--help"]},
    add_completion=False,
)

console = Console(stderr=True)  # All output to stderr to preserve stdout for data


def version_callback(value: bool) -> None:
    """Print version and exit if --version flag is provided."""
    if value:
        typer.echo(f"{{ cookiecutter.command_name }} version {__version__}")
        raise typer.Exit()


def placeholder(stream: TextIO) -> Iterator[str]:
    """Read placeholder from stream

    Args:
        stream: Input stream (file or stdin)

    Yields:
        placeholder
    """
    for line in stream:
        yield "placeholder"


def validate_arguments(
    stats_format: str,
) -> None:
    """Validate argument combinations and constraints.

    Args:
        stats_format: Statistics output format

    Raises:
        typer.BadParameter: If validation fails with clear message
    """

    # Validate stats format
    valid_formats = {"table", "json"}
    if stats_format not in valid_formats:
        raise typer.BadParameter(
            f"--stats-format must be one of {valid_formats}, got '{stats_format}'"
        )


@app.command()
def main(
    input_file: Optional[Path] = typer.Argument(
        None,
        help="Input file to deduplicate (reads from stdin if not specified)",
        exists=True,
        dir_okay=False,
    ),
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
    # Input Format
    placeholder: bool = typer.Option(
        False,
        "--placeholder",
        "-b",
        help="placeholder",
        rich_help_panel="placeholder",
    ),
    # StdErr Control
    quiet: bool = typer.Option(
        False,
        "--quiet",
        "-q",
        help="Suppress statistics output to stderr",
        rich_help_panel="StdErr Control",
    ),
    progress: bool = typer.Option(
        False,
        "--progress",
        "-p",
        help="Show progress indicator (auto-disabled for pipes)",
        rich_help_panel="StdErr Control",
    ),
    stats_format: str = typer.Option(
        "table",
        "--stats-format",
        help="Statistics output format: 'table' (default, Rich table) or 'json' (machine-readable)",
        rich_help_panel="StdErr Control",
    ),
    explain: bool = typer.Option(
        False,
        "--explain",
        "-e",
        help="Show explanations to stderr for why lines were kept or skipped",
        rich_help_panel="StdErr Control",
    ),
) -> None:
    """
    placeholder from streaming input.

    This tool placeholder.

    \b
    Quick Start:
        {{ cookiecutter.command_name }} input.log > output.log              # placeholder a file
        cat placeholder | {{ cookiecutter.command_name }}                          # Use in pipeline

    \b
    More Examples:
        {{ cookiecutter.command_name }} --placeholder
        {{ cookiecutter.command_name }} --quiet input.log > output.log      # No statistics

    \b
    Documentation:
        https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

    \b
    Report Issues:
        https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues
    """
    # Check if running interactively with no input
    if input_file is None and sys.stdin.isatty():
        console.print("[yellow]No input provided.[/yellow]")
        console.print("\n[bold]Usage:[/bold] {{ cookiecutter.command_name }} [FILE] or pipe data via stdin")
        console.print("\n[bold]Examples:[/bold]")
        console.print("  {{ cookiecutter.command_name }} input.log > output.log")
        console.print("  cat placeholder | {{ cookiecutter.command_name }}")
        console.print("\n[dim]For full help: {{ cookiecutter.command_name }} --help[/dim]")
        raise typer.Exit(0)

    # Validate arguments
    validate_arguments(
        stats_format,
    )

    # Disable progress if outputting to a pipe
    show_progress = progress and sys.stdout.isatty()

    if input_file is not None:
        # File mode
        if not quiet:
            console.print(
                "[dim]Auto-detected file input: using placeholder "
                "(override with --placeholder)[/dim]"
            )
    else:
        # Streaming mode
        pass

    if placeholder:
        pass
    else:
        pass


    # Create processor
    processor = {{ cookiecutter.class_name }}(
        explain=explain,
    )

    try:
        # Create progress callback for library monitoring (independent of visual progress)
        progress_callback = None
        if show_progress:
            # Create progress display
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                console=console,
                transient=True,
            ) as progress_bar:
                task = progress_bar.add_task(
                    "Processing placeholder...",
                    total=None,
                    skipped=0,
                )

                def update_progress(line_num: int, lines_skipped: int) -> None:
                    progress_bar.update(
                        task,
                        completed=line_num,
                        skipped=lines_skipped,
                    )

                # Process with progress
                if input_file:
                    with input_file.open("r") as f:
                        processor.process(f, sys.stdout, progress_callback=update_progress)
                else:
                    processor.process(sys.stdin, sys.stdout, progress_callback=update_progress)
        else:
            # Process without progress
            if input_file:
                with input_file.open("r") as f:
                    processor.process(f, sys.stdout, progress_callback=None)
            else:
                processor.process(sys.stdin, sys.stdout, progress_callback=None)

        # Print stats to stderr unless quiet
        if not quiet:
            if stats_format == "json":
                print_stats_json(processor)
            else:
                print_stats(processor)

    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        # Flush what we have
        if placeholder:
            processor.flush(sys.stdout.buffer)
        else:
            processor.flush(sys.stdout)
        if not quiet:
            if stats_format == "json":
                print_stats_json(processor)
            else:
                console.print("[dim]Partial statistics:[/dim]")
                print_stats(processor)
        raise typer.Exit(1) from None
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise typer.Exit(1) from e


def print_stats(processor: {{ cookiecutter.class_name }}) -> None:
    """Print placeholder statistics using rich."""
    stats = processor.get_stats()

    if stats["placeholder"] == 0:
        console.print("[yellow]placeholder[/yellow]")
        return

    # Create stats table
    table = Table(title="placeholder Statistics", show_header=True, header_style="bold cyan")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", justify="right", style="green")

    table.add_row("placeholder", f"{stats['placeholder']:,}")

    console.print()
    console.print(table)
    console.print()


def print_stats_json(processor: {{ cookiecutter.class_name }}) -> None:
    """Print placeholder statistics as JSON to stderr."""
    stats = processor.get_stats()

    output = {
        "statistics": stats,
        "configuration": {
            "placeholder": processor.placeholder,
        },
    }

    # Print to stderr (console already configured for stderr)
    print(json.dumps(output, indent=2), file=sys.stderr)


if __name__ == "__main__":
    app()
