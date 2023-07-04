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
    for key in ["status", "version", "releaseId", "checks"]:
        assert key in payload
    assert payload["status"] == "pass"
    assert payload["version"] == settings.version
    assert payload["releaseId"] == settings.release_id
    for key in ["postgresql:responseTime", "postgresql:uptime"]:
        assert key in payload["checks"]
        for item in payload["checks"][key]:
            assert "componentType" in item
            assert item["componentType"] == "datastore"


@pytest.mark.parametrize(
    "method", ["head", "post", "put", "delete", "options", "patch"]
)
def test_health(method: str) -> None:
    response = operator.methodcaller(method, "/health")(client)
    assert response.status_code == 405
