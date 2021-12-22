.PHONY: lint test all types clean generate

all: lint types test

lint:
	black . --check

test:
	pytest tests

types:
	mypy .


clean:
	rm source/openapi-2.json
	rm -rf bungieapi/generated/

generate: clean
	python -m update --fetch