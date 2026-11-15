from collections.abc import AsyncGenerator

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.core.config import get_settings
from app.models.access_token import AccessToken
from app.models.user import User

_client: AsyncIOMotorClient | None = None


def get_client() -> AsyncIOMotorClient:
    if _client is None:
        raise RuntimeError("MongoDB client is not initialized")
    return _client


def get_db() -> AsyncIOMotorDatabase:
    settings = get_settings()
    return get_client()[settings.mongodb_db_name]


def _patch_motor_append_metadata(client: AsyncIOMotorClient) -> None:
    """Beanie 2.x calls client.append_metadata; Motor may proxy that name as a DB."""
    delegate = getattr(client, "delegate", None)
    if delegate is None or not hasattr(delegate, "append_metadata"):
        return
    # Only patch when Motor did not expose a real bound method on the type.
    if "append_metadata" not in dir(type(client)):
        client.append_metadata = delegate.append_metadata  # type: ignore[attr-defined]


async def connect_to_mongo() -> None:
    global _client
    settings = get_settings()
    _client = AsyncIOMotorClient(
        settings.mongodb_uri,
        uuidRepresentation="standard",
    )
    _patch_motor_append_metadata(_client)
    await init_beanie(
        database=_client[settings.mongodb_db_name],
        document_models=[User, AccessToken],
    )


async def close_mongo_connection() -> None:
    global _client
    if _client is not None:
        _client.close()
        _client = None


async def get_user_db() -> AsyncGenerator:
    from fastapi_users.db import BeanieUserDatabase

    yield BeanieUserDatabase(User)


async def get_access_token_db() -> AsyncGenerator:
    from fastapi_users_db_beanie.access_token import BeanieAccessTokenDatabase

    yield BeanieAccessTokenDatabase(AccessToken)
