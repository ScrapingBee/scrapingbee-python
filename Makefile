install:  ## Install package from source in edit mode
	pip install -e .

deps:  ## Install development dependencies
	pip install -r requiremets.txt

lint:  ## Lint code
	flake8 --config flake8 scrapingbee/ tests/ setup.py

test:  ## Run tests
	pytest tests/