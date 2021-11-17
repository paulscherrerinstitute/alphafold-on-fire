FROM python:3.9 AS development
WORKDIR /usr/src/aof
RUN pip install --no-cache-dir poetry==1.1.11 && poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction --no-ansi
