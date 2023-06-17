import dotenv
import os
from urllib.parse import urlparse


dotenv.load_dotenv()

DEBUG = bool(os.getenv("DEBUG", False))

PORT = int(os.getenv("UVICORN_PORT", 8000))
HOST = os.getenv("UVICORN_HOST", "0.0.0.0")

MAX_CONN = os.getenv("MAX_CONN", 2)
MIN_CONN = os.getenv("MAX_CONN", 1)

parsed_url = urlparse(os.getenv("DATABASE_URL"))

if parsed_url:
    DB_NAME = parsed_url.path[1:]
    DB_USER = parsed_url.username
    DB_PASS = parsed_url.password
    DB_HOST = parsed_url.hostname
    DB_PORT = parsed_url.port
else:
    DB_NAME = os.getenv("PG_DATABASE")
    DB_USER = os.getenv("PG_USER")
    DB_PASS = os.getenv("PG_PASSWORD")
    DB_HOST = os.getenv("PG_HOST")
    DB_PORT = os.getenv("PG_PORT")

ASYNC_DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
