import operator

import pytest
from fastapi import testclient

from app import config, main

client = testclient.TestClient(main.app)
settings = config.get_settings()


def test_get_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/health+json"
    assert response.headers["cache-control"] == "max-age=3600"
    payload = response.json()
    for key in ["status", "version", "releaseId"]:
        assert key in payload
    assert payload["status"] == "pass"
    assert payload["version"] == settings.version
    assert payload["releaseId"] == settings.releaseId


@pytest.mark.parametrize(
    "method", ["head", "post", "put", "delete", "options", "patch"]
)
def test_health(method: str) -> None:
    response = operator.methodcaller(method, "/health")(client)
    assert response.status_code == 405
