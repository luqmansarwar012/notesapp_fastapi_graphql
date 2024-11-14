from mutations.user_mutations import UserMutation
from mutations.note_mutations import NoteMutation
import strawberry


@strawberry.type
class Mutation:
    user_mutation: UserMutation = strawberry.field(resolver=lambda: UserMutation())
    note_mutation: NoteMutation = strawberry.field(resolver=lambda: NoteMutation())
