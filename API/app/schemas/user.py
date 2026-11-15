from beanie import PydanticObjectId
from fastapi_users import schemas
from pydantic import Field


class UserRead(schemas.BaseUser[PydanticObjectId]):
    username: str
    name: str


class UserCreate(schemas.BaseUserCreate):
    username: str = Field(min_length=3, max_length=32, pattern=r"^[a-zA-Z0-9_]+$")
    name: str = Field(min_length=1, max_length=120)


class UserUpdate(schemas.BaseUserUpdate):
    username: str | None = Field(
        default=None,
        min_length=3,
        max_length=32,
        pattern=r"^[a-zA-Z0-9_]+$",
    )
    name: str | None = Field(default=None, min_length=1, max_length=120)
