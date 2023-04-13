install-dev:
	pip install --upgrade pip pip-tools
	pip-sync requirements.txt requirements-dev.txt
  
install:
	pip install --upgrade pip pip-tools
	pip-sync requirements.txt
  
update:
	pip install --upgrade pip pip-tools
	pip-compile requirements.in
	pip-compile requirements-dev.in
	pip-sync requirements.txt requirements-dev.txt

serve:
	python manage.py migrate && python manage.py runserver

lint:
	flake8 palyanytsya
	mypy palyanytsya

black:
	python -m black palyanytsya

clean-imports:
	isort .
	autoflake -r -i --remove-all-unused-imports --ignore-init-module-imports project_name

clean-lint: cleanimports black lint

checkmigrations:
	python manage.py makemigrations --check --no-input --dry-run

test:
	pytest -n 4 -x
