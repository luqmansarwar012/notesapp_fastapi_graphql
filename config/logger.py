import logging

logger = logging.getLogger("APP LOGGER")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(name)10s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
