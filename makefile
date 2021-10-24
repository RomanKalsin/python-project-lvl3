install:
	poetry install
build:
	poetry build
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
lint:
	poetry run flake8 page_loader
page-loader:
	poetry run page-loader
package-install:
	python3 -m pip install --user dist/*.whl
package-uninstall:
	python3 -m pip uninstall hexlet-code