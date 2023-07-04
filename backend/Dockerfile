FROM python:3.10 AS development
WORKDIR /usr/src/aof
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.5.1
ENV PATH="/root/.local/bin:${PATH}"
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi
