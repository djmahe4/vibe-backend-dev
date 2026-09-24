#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen

REPO_ROOT = Path(__file__).resolve().parents[1]
TARGET = REPO_ROOT / "skills" / "vendor"
OWNER = "sickn33"
REPO = "agentic-awesome-skills"

SKILLS = [
    "brainstorming",
    "2slides-ppt-generator",
    "api-design-principles",
    "api-security-best-practices",
    "clean-code",
    "code-showcase-systematic-debugging",
    "executing-plans",
    "docker-expert",
    "github-actions-advanced",
    "fastapi-pro",
    "auth-implementation-patterns",
    "backend-security-coder",
]


def download(url: str) -> str:
    with urlopen(url, timeout=20) as response:  # noqa: S310
        return response.read().decode("utf-8")


def main() -> None:
    TARGET.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []

    for skill in SKILLS:
        destination = TARGET / skill
        destination.mkdir(parents=True, exist_ok=True)
        raw_url = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/main/skills/{skill}/SKILL.md"
        try:
            content = download(raw_url)
        except HTTPError:
            failures.append(skill)
            continue

        (destination / "SKILL.md").write_text(content, encoding="utf-8")

    report = TARGET / "VENDORING_REPORT.md"
    report.write_text(
        "# AAS Vendoring Report\n\n"
        f"Downloaded skills: {len(SKILLS) - len(failures)}\n\n"
        f"Failures: {', '.join(failures) if failures else 'None'}\n",
        encoding="utf-8",
    )

    if failures:
        raise SystemExit(f"Failed to download skills: {', '.join(failures)}")


if __name__ == "__main__":
    main()
