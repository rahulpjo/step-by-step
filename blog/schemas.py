from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
  first_name: str
  last_name: str
  pronouns: str
  email: str
  password: str
  bio: str
  img_url: str = "https://media.istockphoto.com/photos/watercolor-textured-background-picture-id887755698?k=20&m=887755698&s=612x612&w=0&h=UcvMcQg07D_WfBT88iOWWXMV5WMRXRM8nqJRXcySUNA="

class BlogPost(BaseModel):
  body: str
  likes: int = 0
  published: bool = False
  tag: Optional[str] = None
  class Config:
    orm_mode = True
  
class ShowUser(BaseModel):
  first_name: str
  last_name: str
  pronouns: str
  email: str
  bio: str
  img_url: str
  posts: List[BlogPost] = []
  class Config:
    orm_mode = True

class ShowBlogPost(BlogPost):
  author: ShowUser
  class Config:
    orm_mode = True