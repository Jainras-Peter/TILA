"""Auth dependencies — re-export FastAPI Users principals."""

from app.core.users import current_active_user, current_user_optional

__all__ = ["current_active_user", "current_user_optional"]
