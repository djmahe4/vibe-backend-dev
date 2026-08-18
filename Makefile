PYTHON ?= python3

.PHONY: install install-dev run lint typecheck test verify workshop verify-skills aas-dry-run

install:
	$(PYTHON) -m pip install -e .

install-dev:
	$(PYTHON) -m pip install -e .[dev]

run:
	uvicorn app.main:app --reload --app-dir code

lint:
	ruff check code

typecheck:
	mypy code

test:
	pytest code/tests -q

verify: lint typecheck test

workshop:
	@echo "Open README.md and follow the agenda"

aas-dry-run:
	./scripts/install_aas_skills.sh --dry-run

verify-skills:
	./scripts/verify_skills.sh
