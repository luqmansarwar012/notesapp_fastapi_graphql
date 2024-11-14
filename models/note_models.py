from beanie import Document, Link
from models.user_models import User


class Note(Document):
    title: str
    description: str
    user: Link[User]

    class Settings:
        collection = "notes"
