from resolvers.note_resolvers import (
    update_note_resolver,
    delete_note_resolver,
    save_note_resolver,
)
from permissions.is_authenticated import IsAuthenticated
from type.note_types import NoteType
from strawberry.types import Info
import strawberry


@strawberry.type
class NoteMutation:
    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def create_note(self, title: str, description: str, info: Info) -> NoteType:
        user_id = info.context["request"].user_id
        return await save_note_resolver(user_id, title, description)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def update_note(self, note_id: str, title: str, description: str) -> NoteType:
        return await update_note_resolver(note_id, title, description)

    @strawberry.mutation(permission_classes=[IsAuthenticated])
    async def delete_note(self, note_id: str) -> bool:
        return await delete_note_resolver(note_id)
