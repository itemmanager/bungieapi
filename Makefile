.PHONY: lint test all types clean generate reformat
.DEFAULT_GOAL := help

all: lint types test

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

lint: ## use flake8 and black to lint code
	flake8 && black . --check

test: ## run tests
	pytest tests

types: ## run typecheck
	mypy .

reformat: ## reformat code
	isort . && autoflake -i -r . && black .

clean: ## delete all generated files
	rm source/openapi-2.json
	rm -rf bungieapi/generated/

generate: clean ## refetch openapi schema and regenerate client
	python -m update --fetch
	$(MAKE) reformat