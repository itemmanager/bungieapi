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

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"


doc: ## generate documentation
	sphinx-apidoc -o docs/ bungieapi
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

lint: ## use flake8 and black to lint code
	flake8 && black . --check

test: ## run tests
	pytest tests

types: ## run typecheck
	mypy update bungieapi

reformat: ## reformat code
	docformatter . -r -i
	python -m autoflake -i -r --remove-all-unused-imports .
	isort .
	black .

clean: ## delete all generated files
	rm -f source/openapi.json
	rm -rf bungieapi/generated/

generate: clean ## refetch openapi schema and regenerate client
	python -m update --fetch
	$(MAKE) reformat
