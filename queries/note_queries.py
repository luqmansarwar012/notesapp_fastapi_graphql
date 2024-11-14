from permissions.is_authenticated import IsAuthenticated
from resolvers.note_resolvers import get_notes_resolver
from type.note_types import NoteType
from strawberry.types import Info
import strawberry
import typing


@strawberry.type
class NoteQuery:
    @strawberry.field(permission_classes=[IsAuthenticated])
    async def notes(self, info: Info) -> typing.List[NoteType]:
        user_id = info.context["request"].user_id
        return await get_notes_resolver(user_id)
