from type.user_types import UserType
from type.note_types import NoteType
from models.note_models import Note
from models.user_models import User
from bson import ObjectId
from typing import List


async def get_notes_resolver(user_id: str) -> List[NoteType]:
    notes = await Note.find_many(fetch_links=True).to_list()
    return [
        NoteType(
            id=str(note.id),
            title=note.title,
            description=note.description,
            user=UserType(
                id=str(note.user.id), name=note.user.name, email=note.user.email
            ),
        )
        for note in notes
        if note.user.id == ObjectId(user_id)
    ]


async def save_note_resolver(user_id: str, title: str, description: str) -> NoteType:
    user = await User.find_one({"_id": ObjectId(user_id)})
    note = Note(title=title, description=description, user=user)
    await note.save()

    return NoteType(
        id=str(note.id),
        title=note.title,
        description=note.description,
        user=UserType(
            id=str(user.id),
            name=user.name,
            email=user.email,
        ),
    )


async def update_note_resolver(note_id: str, title: str, description: str) -> NoteType:
    note = await Note.find_one({"_id": ObjectId(note_id)}, fetch_links=True)
    if note:
        note.title = title
        note.description = description
        await note.save()
        return NoteType(
            id=str(note.id),
            title=note.title,
            description=note.description,
            user=UserType(
                id=str(note.user.id), name=note.user.name, email=note.user.email
            ),
        )
    raise Exception("Note not found or user not authorized")


async def delete_note_resolver(note_id: str) -> bool:
    note = await Note.find_one({"_id": ObjectId(note_id)})
    if note:
        await note.delete()
        return True
    return False
