PYTEST_CONFIGS := --nomigrations --cov-report=term-missing  --cov-report=html --cov=. --disable-warnings

# Setup
.pip:
		pip install pip --upgrade

setup: .pip
		pip install poetry
		poetry shell
		poetry install

test:
		pytest ${PYTEST_CONFIGS}

code-convention:
		isort .
		black .