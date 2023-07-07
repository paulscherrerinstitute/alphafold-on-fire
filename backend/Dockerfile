FROM python:3.10 AS development
WORKDIR /usr/src/aof
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.5.1
ENV PATH="/root/.local/bin:${PATH}"
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

FROM development AS build
RUN poetry export --without-hashes -o requirements.txt

FROM python:3.10-alpine AS production
WORKDIR /usr/src/aof
ARG VERSION
ARG RELEASE_ID
ENV VERSION=${VERSION} \
    RELEASE_ID=${RELEASE_ID}
RUN python -m pip install --upgrade pip
COPY --from=build /usr/src/aof/requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./alembic ./alembic
COPY alembic.ini ./
COPY ./app ./app
RUN addgroup -S aof && adduser -S aof -G aof
USER aof
EXPOSE 8000
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1
ENTRYPOINT ["/bin/sh", "-c", "uvicorn app.main:app --host 0.0.0.0"]
