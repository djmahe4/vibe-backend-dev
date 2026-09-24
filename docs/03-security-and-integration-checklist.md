# Security and Integration Checklist

## Security defaults
- Input validation for every boundary (Pydantic models).
- JWT secret managed by environment/secret manager.
- `/docs` disabled outside explicit enablement.
- CORS allowlist only.
- Rate limiting on auth and expensive endpoints.
- Least-privilege credentials for DB/cache/external APIs.
- Dependency review and routine updates.

## Integration best practices
- Database sessions via dependency injection.
- Redis/cache guarded by timeout and retry strategy.
- Background tasks isolated and idempotent.
- Outbound HTTP with explicit timeout and circuit breaker pattern.
- Structured logging and request IDs.
- Health/readiness endpoints for orchestrators.
