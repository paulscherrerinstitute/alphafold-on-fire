from fastapi import testclient

from app import config, main

settings = config.get_settings()
client = testclient.TestClient(main.app)


def test_app() -> None:
    assert main.app.title == "alphafold-on-fire"
    assert main.app.version == settings.release_id


def test_get_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello world"}
