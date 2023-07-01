.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m src.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m src.manage makemigrations

.PHONY: superuser
superuser:
	poetry run python -m src.manage createsuperuser

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
	poetry run python -m src.manage runserver

.PHONY: server serve run
.ONESHELL:
server serve run: lint isort runserver

.PHONY: runprod
runprod: install migrate
	poetry run python -m hypercorn src.api.asgi:application --bind 0.0.0.0:8000 --workers 4

.PHONY: shell
shell:
	poetry run python -m src.manage shell