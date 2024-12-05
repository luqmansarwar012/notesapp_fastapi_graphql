from constants.database_constants import MONGODB_URI, DATABASE_NAME
from motor.motor_asyncio import AsyncIOMotorClient
from models.user_models import User
from models.note_models import Note
from beanie import init_beanie
from .logger import logger


async def initiate_database():
    try:
        client = AsyncIOMotorClient(MONGODB_URI)
        await init_beanie(database=client[DATABASE_NAME], document_models=[User, Note])
        return client
    except Exception:
        logger.error("Something went wrong in database service")
        raise
