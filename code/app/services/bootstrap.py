from app.core.security import hash_password
from app.services.user_store import InMemoryUserStore, UserRecord


def seed_default_admin(store: InMemoryUserStore) -> None:
    store.upsert(
        UserRecord(
            username="admin",
            hashed_password=hash_password("ChangeThisNow!123"),
            role="admin",
        )
    )
