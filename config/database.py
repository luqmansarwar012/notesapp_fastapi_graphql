from motor.motor_asyncio import AsyncIOMotorClient
from .constants import MONGODB_URI, DATABASE_NAME
from beanie import init_beanie
from user.models import User
from note.models import Note
from .logger import logger


async def initiate_database():
    try:
        client = AsyncIOMotorClient(MONGODB_URI)
        await init_beanie(database=client[DATABASE_NAME], document_models=[User, Note])
        return client
    except Exception:
        logger.error("Something went wrong in database service")
        raise
