from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
posts = []

class BlogPost(BaseModel):
  name: str
  body: str
  likes: int = 0
  published: bool = False
  tag: Optional[str] = None

# routes and controllers
@app.get("/")
async def index():
  return {"message": "It's time to party!"}

@app.get("/about")
async def about():
  return {"message": "I still unironically like Fun Dip."}

@app.get("/posts")
async def get_posts():
  return {"data": posts}

@app.get("/posts/{id}")
async def get_post(id:int, limit:int = 10, skip: int = 0):
  if id == 20:
    return {"data": f"Time to dance! Limit is {limit} and we have skipped {skip}"}
  else:
    return {"data": f"No, it's {id}. Not the time to dance yet."}

@app.post("/posts")
async def create_post(blog_post: BlogPost):
  return {"message": posts}
