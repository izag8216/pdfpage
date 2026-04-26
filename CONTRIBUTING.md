# Contributing to pdfpage

Thank you for your interest in contributing!

## Development Setup

```bash
git clone https://github.com/izag8216/pdfpage.git
cd pdfpage
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Code Style

- Follow PEP 8 (line length: 100)
- Use type hints for all function signatures
- Write docstrings for public modules and functions

## Commit Convention

```
feat: add new feature
fix: bug fix
docs: documentation change
test: test change
refactor: code refactoring
chore: maintenance
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Make your changes with tests
4. Run `pytest` to ensure quality
5. Push and open a PR