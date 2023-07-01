FROM python:3.11

WORKDIR /app

COPY . .

COPY .env .env

RUN pip install poetry

RUN poetry install

EXPOSE 8000

CMD ["make", "runprod"]