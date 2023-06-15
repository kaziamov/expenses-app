import dotenv
import os
from urllib.parse import urlparse


dotenv.load_dotenv()
MAX_CONN = os.getenv("MAX_CONN", 2)
MIN_CONN = os.getenv("MAX_CONN", 1)

DATABASE_URL = urlparse(os.getenv("DATABASE_URL"))

if DATABASE_URL:
    DB_HOST = DATABASE_URL.hostname
    DB_PORT = DATABASE_URL.port
    DB_NAME = DATABASE_URL.path[1:]
    DB_USER = DATABASE_URL.username
    DB_PASS = DATABASE_URL.password


DB_NAME = os.getenv("PGDATABASE")
DB_USER = os.getenv("PGUSER")
DB_PASS = os.getenv("PGPASSWORD")
DB_HOST = os.getenv("PGHOST")
DB_PORT = os.getenv("PGPORT")
