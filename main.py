from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class BlogPost(BaseModel):
  name: str
  body: str
  likes: int = 0
  published: bool = False
  tag: Optional[str] = None


