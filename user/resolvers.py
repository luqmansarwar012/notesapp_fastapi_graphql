from user.types import UserType
from user.models import User


async def save_user(name: str, email: str, password: str) -> UserType:
    user = User(name=name, email=email, password=password)
    await user.save()

    return UserType(
        id=str(user.id),
        name=user.name,
        email=user.email,
    )
