from .env import get_env_variable


MONGODB_URI = get_env_variable("MONGODB_URI")
DATABASE_NAME = get_env_variable("DATABASE_NAME")
