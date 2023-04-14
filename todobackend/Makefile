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

build-dev:
	docker build -t todoapp .

run-dev:
	docker run --name todoapp \
	-p 8020:8020 \
	-e DJANGO_SUPERUSER_USERNAME=admin \
	-e DJANGO_SUPERUSER_PASSWORD=hello1 \
	-e DJANGO_SUPERUSER_EMAIL=admin@example.com \
	todoapp

restart-dev:
	docker stop todoapp && docker start todoapp

bash-dev:
	docker exec -it todoapp /bin/bash
