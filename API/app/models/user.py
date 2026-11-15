from beanie import Document, Indexed
from fastapi_users.db import BeanieBaseUser


class User(BeanieBaseUser, Document):
    username: Indexed(str, unique=True)
    name: str

    class Settings(BeanieBaseUser.Settings):
        name = "users"
