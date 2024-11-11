from user.models import User
from .types import NoteType
from user.types import UserType
from .models import Note
from typing import List
from bson import ObjectId


async def get_all_notes() -> List[NoteType]:
    notes = await Note.find_all().to_list()
    return [
        NoteType(id=str(note.id), title=note.title, description=note.description)
        for note in notes
    ] or [NoteType(id="dummy id", title="dummy title", description="dummy description")]


async def save_note(user_id: str, title: str, description: str) -> NoteType:
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
