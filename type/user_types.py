from pydantic import BaseModel
from typing import Optional
import strawberry


@strawberry.type
class UserType:
    id: str
    name: str
    email: str


@strawberry.type
class TokenResponse:
    token: str
    token_type: str = "Bearer"


class TokenData(BaseModel):
    user_id: Optional[str] = None
