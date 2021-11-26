# Contributing to alphafold-on-fire
## Backend
### Getting started with Development
The easiest way to start up a dev environment is to use the `docker-compose.dev.yaml` file.
You will need `docker` and `docker-compose` installed as prerequisites.
```console
cd backend/
docker-compose -f docker-compose.dev.yaml up -d --build
```
The app will be exposed on `localhost:8000`.
