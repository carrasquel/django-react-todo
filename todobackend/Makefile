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