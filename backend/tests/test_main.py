from fastapi import testclient

from app import main

client = testclient.TestClient(main.app)


def test_get_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello world"}
