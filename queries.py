from note.resolvers import get_all_notes
from note.types import NoteType
import strawberry
import typing


@strawberry.type
class Query:
    @strawberry.field
    async def notes(self) -> typing.List[NoteType]:
        return await get_all_notes()
