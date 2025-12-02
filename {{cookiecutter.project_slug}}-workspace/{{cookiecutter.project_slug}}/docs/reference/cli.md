# ⚠️ Template doc: Testing disabled ⚠️

# CLI Reference

Complete reference for the `{{ cookiecutter.project_slug }}` command-line interface.

## Command Syntax

```bash
{{ cookiecutter.command_name }} [OPTIONS] [INPUT_FILE]
```

## Basic Usage

```bash
# placeholder
{{ cookiecutter.command_name }} placeholder
```

## Options Reference

### Core Options

#### `--placeholder, -b`
**Type**: placeholder
**Default**: placeholder

placeholder.

```bash
{{ cookiecutter.command_name }} --placeholder
```

### Display Options

#### `--quiet, -q`
**Type**: Boolean
**Default**: False

Suppress statistics output to stderr.

```bash
{{ cookiecutter.command_name }} --quiet input.log
```

#### `--progress, -p`
**Type**: Boolean
**Default**: False

Show progress indicator (auto-disabled for pipes).

```bash
{{ cookiecutter.command_name }} --progress large-file.log
```

#### `--stats-format`
**Type**: String (table | json)
**Default**: table

Statistics output format: 'table' (Rich table) or 'json' (machine-readable).

```bash
{{ cookiecutter.command_name }} --stats-format json input.log
```

#### `--explain`
**Type**: Boolean
**Default**: False

Show explanations to stderr for why placeholder.

Outputs diagnostic messages showing placeholder decisions:
- When placeholder
- Which placeholder

```bash
# See all placeholder decisions
{{ cookiecutter.command_name }} --explain input.log 2> explain.log

# Debug with quiet mode (only explanations, no stats)
{{ cookiecutter.command_name }} --explain --quiet input.log

# Validate placeholder
{{ cookiecutter.command_name }} --explain --placeholder input.log 2>&1 | grep EXPLAIN
```

Example output:
```
EXPLAIN: placeholder
```

See [Explain Mode](../features/explain/explain.md) for detailed usage.

### Version Information

#### `--version`
**Type**: Boolean
**Default**: False

Show version and exit.

```bash
{{ cookiecutter.command_name }} --version
```

Example output:
```
{{ cookiecutter.command_name }} version 0.1.0
```

## Option Combinations

### Mutually Exclusive Options

- `--placeholder` and `--placeholder`: Use one or the other
- `--placeholder` requires `--placeholder`

## Examples

### placeholder

```bash
# placeholder
{{ cookiecutter.command_name }} placeholder.log > output.log
```

## Statistics Output

### Table Format (Default)

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Metric                   ┃  Value ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ placeholder                     │   placeholder │
└──────────────────────────┴────────┘
```

### JSON Format

```json
{
  "statistics": {
    "placeholder": placeholder
  }
}
```

## Exit Codes

- **0**: Success
- **1**: Error (invalid arguments, file not found, processing error)

## See Also

- [{{ cookiecutter.class_name }} API]({{ cookiecutter.command_name }}.md) - Core placeholder class
- [Basic Concepts](../getting-started/basic-concepts.md) - Understanding how {{ cookiecutter.command_name }} works
