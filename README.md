# churnlab-2026

Telco customer churn project for the ESILV Machine Learning Operations course.

## Setup

```sh
uv sync --locked
uv run python -c "import churnlab; print(churnlab.__version__)"
```

## Layout

| Path | Purpose |
|---|---|
| `pyproject.toml` | Project metadata, Python constraint, dependencies |
| `uv.lock` | Resolved package versions |
| `src/churnlab/` | Importable project code |
| `scripts/` | Executable workflow commands |
| `tests/` | Small behavior checks |
| `data/raw/` | Original input snapshot and source metadata |
| `evidence/tp01/` | TP01 submission evidence |
