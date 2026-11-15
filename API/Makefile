.PHONY: run test lint install

VENV ?= venv
PYTHON ?= $(VENV)/bin/python
PIP ?= $(VENV)/bin/pip

install:
	python3.12 -m venv $(VENV)
	$(PIP) install -U pip
	$(PIP) install -e ".[dev]"

run:
	$(VENV)/bin/uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	$(VENV)/bin/pytest

lint:
	$(VENV)/bin/ruff check app tests
