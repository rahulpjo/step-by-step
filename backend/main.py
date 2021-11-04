from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server import models
from server.database import engine
from server.routers import post, user, authentication, photo


app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(photo.router)