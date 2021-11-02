from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(post.router)
app.include_router(user.router)