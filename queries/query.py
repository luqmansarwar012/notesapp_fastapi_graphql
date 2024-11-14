from .note_queries import NoteQuery
import strawberry


@strawberry.type
class Query:
    note_query: NoteQuery = strawberry.field(resolver=lambda: NoteQuery())
