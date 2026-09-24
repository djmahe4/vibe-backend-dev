from dataclasses import dataclass


@dataclass(frozen=True)
class UserRecord:
    username: str
    hashed_password: str
    role: str


class InMemoryUserStore:
    def __init__(self) -> None:
        self._users: dict[str, UserRecord] = {}

    def upsert(self, record: UserRecord) -> None:
        self._users[record.username] = record

    def get(self, username: str) -> UserRecord | None:
        return self._users.get(username)
