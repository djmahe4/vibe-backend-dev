from collections import deque
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta


@dataclass
class SlidingWindowLimiter:
    max_requests_per_minute: int
    buckets: dict[str, deque[datetime]] = field(default_factory=dict)

    def allow(self, key: str) -> bool:
        now = datetime.now(UTC)
        window_start = now - timedelta(minutes=1)
        queue = self.buckets.setdefault(key, deque())

        while queue and queue[0] < window_start:
            queue.popleft()

        if len(queue) >= self.max_requests_per_minute:
            return False

        queue.append(now)
        return True
