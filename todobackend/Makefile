VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

upgrade-pip:
	pip install --upgrade pip pip-tools

install-dev:
	pip install requirements.txt requirements-dev.txt
  
install:
	pip install -r requirements.txt

env:
	python -m venv venv

activate:
	$(VENV)/bin/activate

serve:
	python manage.py migrate && python manage.py runserver

lint:
	flake8 .
	mypy .

black:
	python -m black .

clean:
	rm -rf __pycache__
	rm -rf venv

clean-imports:
	isort .
	autoflake -r -i --remove-all-unused-imports --ignore-init-module-imports .

clean-lint: cleanimports black lint

checkmigrations:
	python manage.py makemigrations --check --no-input --dry-run

test:
	pytest

collect:
	python manage.py collectstatic
