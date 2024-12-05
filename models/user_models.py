from pydantic import EmailStr
from beanie import Document


class User(Document):
    name: str
    email: EmailStr
    password: str

    class Settings:
        collection = "users"
