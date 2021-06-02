install:
	poetry install
lint:
	poetry run flake8 gendiff
test:
	poetry run coverage run --source=gendiff -m pytest tests
cc-coverage:
	poetry run coverage xml
build: lint test
	poetry build