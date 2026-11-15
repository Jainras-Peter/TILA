from fastapi import APIRouter

from app.core.users import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/cookie",
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)


@router.get("/csrf", tags=["auth"])
async def csrf_seed() -> dict[str, bool]:
    """Seed the CSRF cookie for the Angular SPA (double-submit)."""
    return {"ok": True}
