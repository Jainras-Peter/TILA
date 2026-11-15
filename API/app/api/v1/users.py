from fastapi import APIRouter

from app.core.users import fastapi_users
from app.schemas.user import UserRead, UserUpdate

router = APIRouter()

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)
