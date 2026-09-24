#!/usr/bin/env bash
set -euo pipefail

skills=(
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

missing=0
for skill in "${skills[@]}"; do
  if [[ ! -f "skills/vendor/${skill}/SKILL.md" ]]; then
    echo "Missing vendored skill: ${skill}"
    missing=1
  fi
done

if [[ $missing -eq 1 ]]; then
  exit 1
fi

echo "All required skills are vendored."
