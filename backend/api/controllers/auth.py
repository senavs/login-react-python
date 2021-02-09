from datetime import datetime, timedelta

import jwt
from fastapi import Header, HTTPException

from .. import settings
from ..database import ClientConnection, TokenBlacklist, User


def encode(user: dict) -> str:
    payload = {
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=settings.jwt.EXPIRED_MINUTES),
        'user': user
    }
    token = jwt.encode(payload, settings.jwt.SECRET_JEY, algorithm="HS256")

    return token


def decode(token: str) -> dict:
    try:
        user = jwt.decode(token, settings.jwt.SECRET_JEY, algorithms=["HS256"])['user']
    except jwt.ExpiredSignatureError:
        raise HTTPException(403, 'expired token')
    except (jwt.InvalidTokenError, KeyError):
        raise HTTPException(401, 'invalid token')
    return user


def login(username: str, password: str) -> tuple[str, dict]:
    with ClientConnection() as conn:
        if not (user := conn.query(User).filter_by(USERNAME=username).first()):
            raise HTTPException(404, 'user not found')
        if not user.check_password(password):
            raise HTTPException(403, 'wrong password')

        user = user.to_dict(exclude=['PASSWORD', 'CREATED_AT', 'UPDATED_AT'])
        token = encode(user)
    return token, user


def logout(token: str):
    with ClientConnection() as conn:
        if conn.query(TokenBlacklist).filter_by(TOKEN=token).first():
            raise HTTPException(403, 'expired token')
        token_blacklist = TokenBlacklist(TOKEN=token)
        token_blacklist.insert(conn)


def register(username: str, password: str):
    with ClientConnection() as conn:
        if conn.query(User).filter_by(USERNAME=username).first():
            raise HTTPException(404, 'user registered')

        user = User(USERNAME=username, PASSWORD=password)
        user.insert(conn)
        result = user.to_dict()
    return result


def login_required(authentication: str = Header(..., alias='Authenticate')) -> [str, dict]:
    bearer_token = authentication.split(' ', maxsplit=2)

    if len(bearer_token) != 2 or bearer_token[0].lower() != 'bearer':
        raise HTTPException(401, 'invalid token')
    else:
        _, token = bearer_token

    with ClientConnection() as conn:
        if conn.query(TokenBlacklist).filter_by(TOKEN=token).first():
            raise HTTPException(403, 'expired token')

    user = decode(token)
    return token, user
