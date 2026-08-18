from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.config import Settings, get_settings
from app.core.rate_limit import SlidingWindowLimiter
from app.core.security import decode_access_token
from app.services.user_store import InMemoryUserStore

bearer = HTTPBearer(auto_error=False)


def get_user_store(request: Request) -> InMemoryUserStore:
    return request.app.state.user_store  # type: ignore[no-any-return]


def get_limiter(request: Request) -> SlidingWindowLimiter:
    return request.app.state.limiter  # type: ignore[no-any-return]


def get_current_subject(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer),
    settings: Settings = Depends(get_settings),
) -> str:
    if credentials is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")

    subject = decode_access_token(credentials.credentials, settings)
    if subject is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    return subject
