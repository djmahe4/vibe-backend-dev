from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.api.deps import get_current_subject, get_limiter, get_user_store
from app.api.schemas import (
    HealthResponse,
    LoginRequest,
    PromptRequest,
    PromptResponse,
    TokenResponse,
)
from app.core.config import Settings, get_settings
from app.core.rate_limit import SlidingWindowLimiter
from app.core.security import create_access_token, verify_password
from app.services.user_store import InMemoryUserStore

router = APIRouter(prefix="/api/v1", tags=["workshop"])


@router.get("/health", response_model=HealthResponse)
def health(settings: Settings = Depends(get_settings)) -> HealthResponse:
    return HealthResponse(status="ok", environment=settings.environment)


@router.post("/auth/token", response_model=TokenResponse)
def login(
    body: LoginRequest,
    request: Request,
    settings: Settings = Depends(get_settings),
    users: InMemoryUserStore = Depends(get_user_store),
) -> TokenResponse:
    client_key = request.client.host if request.client else "unknown"
    limiter: SlidingWindowLimiter = get_limiter(request)
    if not limiter.allow(f"login:{client_key}"):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded",
        )

    record = users.get(body.username)
    if record is None or not verify_password(body.password, record.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return TokenResponse(access_token=create_access_token(record.username, settings=settings))


@router.post("/vibe/intent", response_model=PromptResponse)
def vibe_intent(
    body: PromptRequest,
    subject: str = Depends(get_current_subject),
) -> PromptResponse:
    route_name = body.intent.lower().replace(" ", "-")[:42]
    return PromptResponse(
        summary=f"Intent accepted for {subject}: {body.intent}",
        generated_route_name=route_name,
        security_notes=[
            "Validate payloads with Pydantic before execution.",
            "Apply authorization rules before side-effects.",
            "Use rate limiting for prompt-triggered endpoints.",
        ],
    )
