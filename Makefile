.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m core.manage makemigrations

.PHONY: superuser
superuser:
	poetry run python -m core.manage createsuperuser

.PHONY: update
update: 
	install migrate;

.PHONY: lint
lint: 
	poetry run blue .

.PHONY: isort
isort: 
	poetry run isort .

.PHONY: runserver
runserver:
	poetry run python -m core.manage runserver

.PHONY: server serve run
.ONESHELL:
server serve run: lint isort runserver

.PHONY: runprod
runprod: install migrate
	poetry run python -m hypercorn core.api.asgi:application --bind 0.0.0.0:8000 --workers 4