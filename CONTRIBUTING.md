# Contributing to alphafold-on-fire
## Backend
### Getting started with Development
The easiest way to start up a dev environment is to use the `docker-compose.dev.yaml` file.
You will need `docker` and `docker-compose` installed as prerequisites.
```console
cd backend/
docker-compose up -d --build
```
The app will be exposed on `localhost:8000`.

### Keycloak
Users:
```json
[
  {
    "username": "jane",
    "password": "jane"
  }
]
```

How to export the keycloak realm:
```console
docker exec -it keycloak-aof /opt/jboss/keycloak/bin/standalone.sh \
-Djboss.socket.binding.port-offset=100 -Dkeycloak.migration.action=export \
-Dkeycloak.migration.provider=singleFile \
-Dkeycloak.migration.realmName=dev \
-Dkeycloak.migration.usersExportStrategy=REALM_FILE \
-Dkeycloak.migration.file=/tmp/io/dev-realm.json
```
