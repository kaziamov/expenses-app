import uvicorn
from database import init_pool_lock
from app import app
from settings import PORT, HOST


if __name__ == "__main__":
    init_pool_lock()
    uvicorn.run(app, port=PORT, host=HOST)
