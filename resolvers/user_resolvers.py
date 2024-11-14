from constants.jwt_constants import EXPIRATION, JWT_SECRET
from datetime import datetime, timedelta, timezone
from helpers.user_helpers import authenticate_user
from type.user_types import UserType
from models.user_models import User
import jwt


async def save_user_resolver(name: str, email: str, password: str) -> UserType:
    user = User(name=name, email=email, password=password)
    await user.save()

    return UserType(
        id=str(user.id),
        name=user.name,
        email=user.email,
    )


async def create_token_resolver(email: str, password: str):
    user = await authenticate_user(email=email, password=password)
    expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRATION)
    payload = {
        "sub": str(user.id),
        "exp": expire,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")

    return {"token": token, "token_type": "Bearer"}
