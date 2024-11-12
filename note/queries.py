from .resolvers import get_all_notes
from .types import NoteType
import strawberry
import typing


@strawberry.type
class NoteQuery:
    @strawberry.field
    async def notes(self, user_id: str) -> typing.List[NoteType]:
        return await get_all_notes(user_id)
