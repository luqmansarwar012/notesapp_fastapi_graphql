from .resolvers import update_note_by_note_id, delete_note_by_note_id, save_note
from .types import NoteType
import strawberry


@strawberry.type
class NoteMutation:
    @strawberry.mutation
    async def create_note(self, user_id: str, title: str, description: str) -> NoteType:
        return await save_note(user_id, title, description)

    @strawberry.mutation
    async def update_note(self, note_id: str, title: str, description: str) -> NoteType:
        return await update_note_by_note_id(note_id, title, description)

    @strawberry.mutation
    async def delete_note(self, note_id: str) -> bool:
        return await delete_note_by_note_id(note_id)
