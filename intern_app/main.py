from fastapi import FastAPI
from intern_app.routers.auth import router
from .database import Base,engine

app=FastAPI()

app.include_router(router, tags=["Auth"])
Base.metadata.create_all(bind=engine)