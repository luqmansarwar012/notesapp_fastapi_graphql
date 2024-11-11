from user.resolvers import save_user
from note.resolvers import save_note
from note.types import NoteType
from user.types import UserType
import strawberry


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_user(self, name: str, email: str, password: str) -> UserType:
        return await save_user(name, email, password)

    @strawberry.mutation
    async def create_note(self, user_id: str, title: str, description: str) -> NoteType:
        return await save_note(user_id, title, description)
