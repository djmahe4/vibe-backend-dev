# 🚀 Vibe Backend Dev Workshop (FastAPI + Agentic Workflows)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-typed%20and%20async-009688)
![CI](https://img.shields.io/github/actions/workflow/status/djmahe4/vibe-backend-dev/ci.yml?label=CI)

> A production-minded, 1-day interactive workshop repo for **intent-driven (“vibe”) backend development** with FastAPI and agentic skills.

<p align="center">
  <img src="https://media.giphy.com/media/QMHoU66sBXqqLqYvGO/giphy.gif" width="300" alt="This is fine gif" />
  <img src="https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif" width="250" alt="Success kid gif" />
</p>

## ⚡ Quick start

```bash
python -m pip install -e .[dev]
make verify
make run
```

## 🧭 Workshop navigation

- [Agenda](docs/01-workshop-agenda.md)
- [FastAPI vs other stacks](docs/02-tech-comparisons.md)
- [Security + integration checklist](docs/03-security-and-integration-checklist.md)
- [Slide deck markdown](presentation/workshop-slides.md)

<details>
<summary><strong>🆚 FastAPI vs Flask/Django/Nest/Go/Spring (workshop quick matrix)</strong></summary>

| Stack | DX | Type Safety | Async Story | Auto Docs | Best fit |
|---|---|---|---|---|---|
| FastAPI | Excellent | Native via Python hints + Pydantic | Native | OpenAPI built-in | API-first, rapid iteration |
| Flask | Flexible | Optional/manual | Optional | Manual | Small custom services |
| Django | Batteries-included | Moderate | Improving | Partial/manual | Full-featured monoliths |
| NestJS | Structured | Strong (TS) | Strong | Good | TS-heavy backend teams |
| Go (Gin/Fiber) | Good | Compile-time | Strong | Manual/third-party | High-performance services |
| Spring Boot | Mature enterprise | Strong | Strong | Good | Large JVM ecosystems |

</details>

<details>
<summary><strong>🎯 Vibe exercise path (intent → typed endpoint)</strong></summary>

1. State intent: “Create secure tenant metrics endpoint.”
2. Model request/response with Pydantic.
3. Add auth dependency + authorization rule.
4. Add rate limiting + tests.
5. Validate with `make verify`.

</details>

## 🛠️ Demo API (secure defaults)

- Typed schemas for all request/response models.
- JWT auth flow.
- `/docs` disabled by default.
- CORS allowlist and minimal methods.
- Simple sliding-window limiter for auth endpoint.

### Endpoints
- `GET /api/v1/health`
- `POST /api/v1/auth/token`
- `POST /api/v1/vibe/intent` (requires bearer token)

## 🤖 Agentic Awesome Skills (AAS) integration

- Skills metadata: [`aas-stack.json`](aas-stack.json)
- Vendored skills path: [`skills/vendor`](skills/vendor)
- Dry-run install:
  ```bash
  make aas-dry-run
  ```
- Vendor selected SKILL.md files:
  ```bash
  python scripts/vendor_aas_skills.py
  make verify-skills
  ```
- Invocation style in agent systems: `@brainstorming`, `@api-security-best-practices`, `@fastapi-pro`

> ⚠️ Risk note: avoid full-catalog installs in constrained-context systems (e.g., Antigravity); use exact IDs.

## 😄 Meme lane (because learning should be fun)

- “This is fine” for tech debt moments.
- “Success kid” for green CI.
- [Attribution links](assets/memes/attribution.md)

## 🧪 Quality gates

```bash
make lint
make typecheck
make test
```

## 📦 Production-minded next steps

- Replace in-memory store with PostgreSQL + SQLModel.
- Add Redis-based distributed rate limiting.
- Add role-based authorization policy engine.
- Add OpenTelemetry traces and structured logs.
