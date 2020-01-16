.PHONY: requirements

# Set environment variables
ENVIRONMENT = set -o allexport; . ./.env; set +o allexport;

# Set the following variable to you project name
PROJECT_NAME = bare
WEB_APP = task_access
DEFAULT_VIRTUALENV = .venv
# Possible virtualenv if virtualenvwrapper is used
POSSIBLE_VIRTUALENV = $(VIRTUAL_ENV)
# Use possible virtualenv if it exists and virtualenvwrapper is used, otherwise use default one
VIRTUALENV = $(if $(wildcard $(POSSIBLE_VIRTUALENV)),$(POSSIBLE_VIRTUALENV),$(DEFAULT_VIRTUALENV))

PYVERSION=3.7
PIP = $(VIRTUALENV)/bin/pip
PYTHON = $(VIRTUALENV)/bin/python

venv:
	@echo "Creating virtual environment within \"$(VIRTUALENV)\" directory"
	@python$(PYVERSION) -m venv $(VIRTUALENV) || rm -rf $(VIRTUALENV) && virtualenv -p `which python$(PYVERSION)` $(VIRTUALENV)

environment:
	@echo "python version"
	@echo "$(PYVERSION)"

requirements:
	@echo "Installing $(PROJECT_NAME) requirements dev..."
	@$(PIP) install -r requirements.txt

migrate_task:
	@echo "Migrating data from task_data.csv to database..."
	@$(PYTHON) migrate_task_data.py

run:
	@echo "Starting App foreground..."
	@$(PYTHON) $(WEB_APP)/views.py

run_background:
	@echo "Starting App background..."
	@$(PYTHON) $(WEB_APP)/views.py &
