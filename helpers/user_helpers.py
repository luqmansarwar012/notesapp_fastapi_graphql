from models.user_models import User
from constants.jwt_constants import JWT_SECRET
import jwt
from bson import ObjectId


async def authenticate_user(email, password):
    user = await User.find_one(User.email == email)
    if not user or user.password != password:
        raise ValueError("Invalid email or password")
    return user


async def get_user(user_id: str):
    try:
        user = await User.find_one({"_id": ObjectId(user_id)})
        if not user:
            return None
        return user
    except:
        raise ValueError("Invalid user ID format")


def verify_token(token: str) -> bool:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user_id: str = payload.get("sub")

        if not user_id:
            return None

        return user_id
    except Exception:
        raise Exception("Something went wrong in verifying the token")
