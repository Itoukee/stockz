from datetime import datetime, timedelta, timezone
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException
import jwt

from settings import settings


security = HTTPBearer()


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.jwt_expire_min)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.jwt_key, algorithm=settings.jwt_algo)


def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.jwt_key, algorithms=[settings.jwt_algo])
        return payload
    except jwt.PyJWTError:
        return None


def require_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = verify_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return payload
