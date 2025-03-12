from fastapi import FastAPI
import uvicorn
from api.endpoints import router as api_router
from database.connection import engine
from database.models import Base
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Finance App", lifespan=lifespan)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("database.main:app", host="127.0.0.1", port=8000, reload=True)
