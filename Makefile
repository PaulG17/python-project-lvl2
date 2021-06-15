install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run coverage run --source=gendiff -m pytest tests

cc-coverage:
	poetry run coverage xml

build: 
	lint
	test 
	poetry build

package-install: 
	build python3 -m pip install --user dist/*.whl

publish: 
	build poetry publish -r testpypi

