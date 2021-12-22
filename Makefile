.PHONY: lint test all types clean generate reformat

all: lint types test

lint:
	black . --check

test:
	pytest tests

types:
	mypy .

reformat:
	isort . && autoflake -i -r . && black .

clean:
	rm source/openapi-2.json
	rm -rf bungieapi/generated/

generate: clean
	python -m update --fetch