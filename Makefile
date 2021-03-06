install:
	@poetry install

lint:
	@poetry run flake8 page_loader

run_test:
	@poetry run pytest -vv --cov=page_loader tests/ --cov-report xml

.PHONY: install lint test
