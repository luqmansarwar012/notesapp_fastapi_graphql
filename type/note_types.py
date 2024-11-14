from type.user_typess import UserType
import strawberry


@strawberry.type
class NoteType:
    id: str
    title: str
    description: str
    user: UserType
