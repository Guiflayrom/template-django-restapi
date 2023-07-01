# Instalation:

## Windows
- Install Python 3.11 [HERE](https://www.python.org/downloads/)
- Create a virtualenv with `virtualenv venv`
- Activate virtualenv with: `venv/Scripts/activate.bat`
- Install poetry with: `pip install poetry`
- Install packages with poetry: `poetry install`
- Finally to start you can type: `poetry run python -m core.manage runserver` or just `make serve(r)`

## Docker

### To Start

- docker compose -f docker-compose.dev.yml up -d
- docker compose -f docker-compose.prod.yml up -d

### To Stop

- docker compose -f docker-compose.dev.yml down
- docker compose -f docker-compose.prod.yml down