import fastapi
import pytest
import requests

from app import config, security

settings = config.get_settings()

_expired_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2S2tadDd5V3hwbVhyNlphWTk1TEtmUDNNdnFxWlZPUmhTZEVrNDVjYzVnIn0.eyJleHAiOjE2NDMyNzQ2MzgsImlhdCI6MTY0MzI3NDMzOCwiYXV0aF90aW1lIjoxNjQzMjc0MzM4LCJqdGkiOiIxNWE0OTY4OS0yMmZlLTRjYTktYjcxMS1kNmVmNDdjZThhYTYiLCJpc3MiOiJodHRwOi8vaG9zdC5kb2NrZXIuaW50ZXJuYWw6ODA4MC9hdXRoL3JlYWxtcy9kZXYiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiNjE5Y2Y5YzUtNWYzNy00N2E1LWFhZTgtNGE2MTk1NjkwYzc0IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYWxwaGFmb2xkLW9uLWZpcmUiLCJzZXNzaW9uX3N0YXRlIjoiNzk3OWE1YjgtOTE4NS00MzIwLTgwYmEtZjQzYzJkYmU3N2ZjIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwOi8vbG9jYWxob3N0OjgwMDAiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtZGV2Iiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiI3OTc5YTViOC05MTg1LTQzMjAtODBiYS1mNDNjMmRiZTc3ZmMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkphbmUgRG9lIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiamFuZSIsImdpdmVuX25hbWUiOiJKYW5lIiwiZmFtaWx5X25hbWUiOiJEb2UiLCJlbWFpbCI6ImphbmUuZG9lQGRldi5jb20ifQ.Na5RRRCbbO0YisGk8FqGA-erQRS3RoKqHRmSUiWQC2fO-TVt5SupRHzSN8ssnI0tbjDCTi3xTTXeZfOPnLg5bNtWTSbtQkupvrNJUjpM3PeD2zZL8aGpVRWQ1XVOP1wQsclt-8da6enWG1OHlgMtigoNzuMmtZauOivCJnkLBqJB69Eoun02O86RRaFdTtW5lv8ypn8bq6XHwGVTFbeBJRpb9S-s4Hzj4bRkgdAQl7wBiJnsXcBoY-xBU9UbIySxaIYhZ8yAeHirpvKXh16M3i47Ce_5f8b_ZdDxJ5ZzYi82s4pAV5-XZZq8kjhm5zy2wvlb4ra5K_S2Wyfbo2orAA"  # noqa: E501
_no_iss_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"  # noqa: E501
_fake_iss_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0Ojg4ODgvYXV0aC9yZWFsbXMvZG9lcy1ub3QtZXhpc3QifQ.gpM3Ya0BheWvPXKDQ-Ezgkh5lUh6mdXBtdqSo_mjFFE"  # noqa: E501


def _get_valid_token() -> str:
    token_url = f"{settings.auth_server}/protocol/openid-connect/token"
    data = {
        "grant_type": "password",
        "client_id": "alphafold-frontend",
        "username": "jane",
        "password": "jane",
    }
    response = requests.post(token_url, data=data)
    return str(response.json()["access_token"])


@pytest.mark.parametrize("clear_cache", [True, False])
def test__get_jwks_no_auth_server(clear_cache: bool) -> None:
    url = "http://localhost:8888"  # no auth server here
    with pytest.raises(fastapi.HTTPException) as excinfo:
        _ = security._get_jwks(url=url)
    assert security._auth_server_exception == excinfo.value


def test__get_jwks() -> None:
    url = f"{settings.auth_server}/.well-known/openid-configuration"
    jwks = security._get_jwks(url=url, clear_cache=True)
    assert "keys" in jwks


@pytest.mark.parametrize(
    "token", [None, _expired_token, _no_iss_token, _fake_iss_token]
)
def test_get_claims_invalid_token(token: str | None) -> None:
    with pytest.raises(fastapi.HTTPException) as excinfo:
        _ = security.get_claims(token=token, settings=settings)
    assert security._invalid_token_exception == excinfo.value


def test_get_claims_invalid_audience() -> None:
    no_aud_settings = settings.copy(update={"audience": "invalid"}, deep=True)
    with pytest.raises(fastapi.HTTPException) as excinfo:
        _ = security.get_claims(token=_get_valid_token(), settings=no_aud_settings)
    assert security._invalid_token_exception == excinfo.value


def test_get_claims_token() -> None:
    claims = security.get_claims(token=_get_valid_token(), settings=settings)
    for key in ["azp", "resource_access", "email"]:
        assert key in claims
