from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
  first_name: str
  last_name: str
  img_url: str


class BlogPost(BaseModel):
  body: str
  likes: int = 0
  published: bool = False
  tag: Optional[str] = None

class ShowBlogPost(BlogPost):
  pass
  class Config():
    orm_mode = True