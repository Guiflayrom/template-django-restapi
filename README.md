# Instalation:

## Windows
- Install Python 3.11 [HERE](https://www.python.org/downloads/)
- Create a virtualenv with `virtualenv venv`
- Activate virtualenv with: `venv/Scripts/activate.bat`
- Install poetry with: `pip install poetry`
- Install packages with poetry: `poetry install`
- Finally to start you can type: `poetry run python -m core.manage runserver` or just `make serve(r)`

## Docker
- docker build -t socio-backend .
- docker run -d -p 8000:8000 socio-backend
