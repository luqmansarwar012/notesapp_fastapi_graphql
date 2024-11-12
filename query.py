from note.resolvers import get_all_notes
from note.types import NoteType
import strawberry
import typing
from user.queries import UserQuery
from note.queries import NoteQuery


@strawberry.type
class Query:
    user_query: UserQuery = strawberry.field(resolver=lambda: UserQuery())
    note_query: NoteQuery = strawberry.field(resolver=lambda: NoteQuery())
