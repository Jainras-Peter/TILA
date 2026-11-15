from collections.abc import AsyncGenerator

from beanie import PydanticObjectId
from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users import BaseUserManager, FastAPIUsers, exceptions
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
)
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy
from fastapi_users.db import BeanieUserDatabase, ObjectIDIDMixin

from app.core.config import get_settings
from app.core.database import get_access_token_db, get_user_db
from app.models.access_token import AccessToken
from app.models.user import User
from app.schemas.user import UserCreate


class UserManager(ObjectIDIDMixin, BaseUserManager[User, PydanticObjectId]):
    reset_password_token_secret = get_settings().auth_secret
    verification_token_secret = get_settings().auth_secret

    async def create(
        self,
        user_create: UserCreate,
        safe: bool = False,
        request: Request | None = None,
    ) -> User:
        existing = await User.find_one(User.username == user_create.username)
        if existing is not None:
            raise exceptions.UserAlreadyExists()
        return await super().create(user_create, safe=safe, request=request)

    async def authenticate(
        self, credentials: OAuth2PasswordRequestForm
    ) -> User | None:
        user = await User.find_one(User.username == credentials.username)
        if user is None:
            self.password_helper.hash(credentials.password)
            return None

        verified, updated_password_hash = self.password_helper.verify_and_update(
            credentials.password, user.hashed_password
        )
        if not verified:
            return None
        if updated_password_hash is not None:
            await self.user_db.update(user, {"hashed_password": updated_password_hash})
        return user


async def get_user_manager(
    user_db: BeanieUserDatabase[User] = Depends(get_user_db),  # noqa: B008
) -> AsyncGenerator[UserManager, None]:
    yield UserManager(user_db)


def _cookie_transport() -> CookieTransport:
    settings = get_settings()
    return CookieTransport(
        cookie_name=settings.auth_cookie_name,
        cookie_max_age=settings.auth_cookie_max_age,
        cookie_httponly=True,
        cookie_samesite="lax",
        cookie_secure=settings.is_production,
    )


def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(  # noqa: B008
        get_access_token_db
    ),
) -> DatabaseStrategy[User, PydanticObjectId, AccessToken]:
    settings = get_settings()
    return DatabaseStrategy(
        access_token_db,
        lifetime_seconds=settings.auth_cookie_max_age,
    )


auth_backend = AuthenticationBackend(
    name="cookie",
    transport=_cookie_transport(),
    get_strategy=get_database_strategy,
)

fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
current_user_optional = fastapi_users.current_user(active=True, optional=True)
