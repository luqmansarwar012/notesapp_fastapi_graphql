from .resolvers import save_user
from .types import UserType
import strawberry


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def create_user(self, name: str, email: str, password: str) -> UserType:
        return await save_user(name, email, password)
