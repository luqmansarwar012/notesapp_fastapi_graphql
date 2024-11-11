from beanie import Document, Link
from user.models import User


class Note(Document):
    title: str
    description: str
    user: Link[User]

    class Settings:
        collection = "notes"
