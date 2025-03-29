.PHONY: install clean test lint build run

# Python settings
PYTHON = python3
VENV = .venv
BIN = $(VENV)/bin

# Project settings
PROJECT = stocks
SRC_DIR = src
TEST_DIR = tests

# Installation targets
install: $(VENV)/bin/activate
	$(BIN)/pip install -e ".[dev]"

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip

# Development targets
clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

test:
	$(BIN)/pytest $(TEST_DIR) -v --cov=$(SRC_DIR)

lint:
	$(BIN)/black $(SRC_DIR)
	$(BIN)/pylint $(SRC_DIR)

format:
	$(BIN)/isort $(SRC_DIR)
	$(BIN)/black $(SRC_DIR)

check:
	$(BIN)/pre-commit run --all-files

coverage:
	$(BIN)/pytest --cov=$(SRC_DIR) --cov-report=html tests/

typecheck:
	$(BIN)/mypy $(SRC_DIR)

validate: typecheck lint test
	
# Build and run targets
build:
	$(BIN)/pyinstaller --clean stocks.spec

run:
	$(BIN)/python $(SRC_DIR)/main.py