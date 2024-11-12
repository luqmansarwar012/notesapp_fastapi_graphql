from user.mutations import UserMutation
from note.mutations import NoteMutation
import strawberry


@strawberry.type
class Mutation:
    user_mutation: UserMutation = strawberry.field(resolver=lambda: UserMutation())
    note_mutation: NoteMutation = strawberry.field(resolver=lambda: NoteMutation())
