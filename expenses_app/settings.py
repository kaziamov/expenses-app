import dotenv
import os
from urllib.parse import urlparse


dotenv.load_dotenv()

PORT = int(os.getenv("PORT", 8000))
HOST = os.getenv("HOST", "0.0.0.0")

MAX_CONN = os.getenv("MAX_CONN", 2)
MIN_CONN = os.getenv("MAX_CONN", 1)

DATABASE_URL = urlparse(os.getenv("DATABASE_URL"))

if DATABASE_URL:
    DB_HOST = DATABASE_URL.hostname
    DB_PORT = DATABASE_URL.port
    DB_NAME = DATABASE_URL.path[1:]
    DB_USER = DATABASE_URL.username
    DB_PASS = DATABASE_URL.password
else:
    DB_NAME = os.getenv("PG_DATABASE")
    DB_USER = os.getenv("PG_USER")
    DB_PASS = os.getenv("PG_PASSWORD")
    DB_HOST = os.getenv("PG_HOST")
    DB_PORT = os.getenv("PG_PORT")
