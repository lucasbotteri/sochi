from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import api

from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

## Statics Files
app.mount("/files", StaticFiles(directory="files"), name="files")

## Routes
app.include_router(api.router)


