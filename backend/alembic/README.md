# Getting started with Alembic

We are using a single-database configuration with an async dbapi.

How to create a new revision
```console
alembic revision --autogenerate -m '<revision name>'
```

How to upgrade the database to the latest version
```console
alembic upgrade head
```

How to downgrade the database one version
```console
alembic downgrade -1
```

How to downgrade the database to zero
```console
alembic downgrade base
```
