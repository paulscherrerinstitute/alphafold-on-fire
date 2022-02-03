from typing import Any

import fastapi
import requests_cache
from fastapi import security
from jose import exceptions, jwt

from app import config

settings = config.get_settings()

_oauth_scheme = security.OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{settings.auth_server[0]}/protocol/openid-connect/auth",
    tokenUrl=f"{settings.auth_server[0]}/protocol/openid-connect/token",
)


_auth_server_exception = fastapi.HTTPException(
    status_code=500, detail="Could not get JWK set from auth server"
)
_invalid_token_exception = fastapi.HTTPException(
    status_code=401,
    detail="Invalid token",
    headers={"WWW-Authenticate": "Bearer"},
)


def _get_jwks(url: str, clear_cache: bool = False) -> Any:
    try:
        with requests_cache.CachedSession(
            backend="memory", expire_after=3600, cache_control=True
        ) as session:
            if clear_cache:
                session.cache.clear()
            response = session.get(url=url)
            payload = response.json()
            response = session.get(url=payload["jwks_uri"])
            jwks = response.json()
    except Exception:
        raise _auth_server_exception
    return jwks


def get_claims(
    token: str = fastapi.Depends(_oauth_scheme),
    settings: config.Settings = fastapi.Depends(config.get_settings),
) -> Any:
    try:
        claims = jwt.get_unverified_claims(token)
    except exceptions.JWTError:
        raise _invalid_token_exception

    if claims.get("iss") not in settings.auth_server:
        raise _invalid_token_exception

    url = f"{claims['iss']}/.well-known/openid-configuration"
    jwks = _get_jwks(url)
    try:
        claims = jwt.decode(
            token, jwks, audience=settings.audience, issuer=settings.auth_server
        )
    except exceptions.JWTError:
        raise _invalid_token_exception

    return claims
