VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

install-dev:
	pip install --upgrade pip pip-tools
	pip-sync requirements.txt requirements-dev.txt
  
install:
	pip install --upgrade pip pip-tools
	pip-sync requirements.txt

env:
	python -m venv venv

activate:
	$(VENV)/bin/activate

serve:
	python manage.py migrate && python manage.py runserver

lint:
	flake8 palyanytsya
	mypy palyanytsya

black:
	python -m black palyanytsya

clean:
	rm -rf __pycache__
	rm -rf venv

clean-imports:
	isort .
	autoflake -r -i --remove-all-unused-imports --ignore-init-module-imports project_name

clean-lint: cleanimports black lint

checkmigrations:
	python manage.py makemigrations --check --no-input --dry-run

test:
	pytest -n 4 -x