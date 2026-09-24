#!/usr/bin/env bash
set -euo pipefail

SKILLS=(
  brainstorming
  2slides-ppt-generator
  api-design-principles
  api-security-best-practices
  clean-code
  code-showcase-systematic-debugging
  executing-plans
  docker-expert
  github-actions-advanced
  fastapi-pro
  auth-implementation-patterns
  backend-security-coder
)

if [[ "${1:-}" == "--dry-run" ]]; then
  printf 'npx agentic-awesome-skills --skills %s\n' "$(IFS=,; echo "${SKILLS[*]}")"
  exit 0
fi

echo "Installing exact skill list for controlled context usage..."
npx agentic-awesome-skills --skills "$(IFS=,; echo "${SKILLS[*]}")"
