import strawberry


@strawberry.type
class UserQuery:
    @strawberry.field
    async def test() -> str:
        return "test"
