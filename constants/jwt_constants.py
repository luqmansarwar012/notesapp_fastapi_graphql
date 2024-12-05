from config.env import get_env_variable

JWT_SECRET = get_env_variable("JWT_SECRET")
EXPIRATION = int(get_env_variable("EXPIRATION"))
