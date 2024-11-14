from ..resolvers.user_resolvers import save_user_resolver, create_token_resolver
from ..types.user_types import UserType, TokenResponse
import strawberry


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def login(self, email: str, password: str) -> TokenResponse:
        result = await create_token_resolver(email, password)
        return TokenResponse(**result)

    @strawberry.mutation
    async def create_user(self, name: str, email: str, password: str) -> UserType:
        return await save_user_resolver(name, email, password)
