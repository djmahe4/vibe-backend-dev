from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    environment: str


class LoginRequest(BaseModel):
    username: str = Field(min_length=3, max_length=64)
    password: str = Field(min_length=12, max_length=128)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class PromptRequest(BaseModel):
    intent: str = Field(min_length=3, max_length=300)


class PromptResponse(BaseModel):
    summary: str
    generated_route_name: str
    security_notes: list[str]
