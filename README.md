# Testing Python Project

A Python project using uv for dependency management and pytest for testing.

## Prerequisites

- Python 3.14
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

Install dependencies using uv:

```bash
uv sync
```

## Running Tests

Run all tests with pytest:

```bash
uv run pytest
```

Run tests with verbose output:

```bash
uv run pytest -v
```

Run a specific test file:

```bash
uv run pytest tests/first_test.py
```

Run tests with coverage:

```bash
uv run pytest --cov
```

## Project Structure

```
.
├── config.py
├── tests/
│   ├── __init__.py
│   └── first_test.py
├── pytest.ini
├── pyproject.toml
└── uv.lock
```

## Configuration

- `pyproject.toml` - Project dependencies and metadata
- `pytest.ini` - Pytest configuration
- `.env.example` - Environment variables template
