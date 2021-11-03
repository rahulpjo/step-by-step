from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class PostORM(Base):
  __tablename__ = "posts"
  id = Column(Integer, primary_key=True, index=True)
  body = Column(String)
  likes = Column(Integer)
  published = Column(Boolean)
  tag = Column(String)
  author_id = Column(Integer, ForeignKey("users.id"))
  
  author = relationship("UserORM", back_populates="posts")

class UserORM(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  first_name = Column(String)
  last_name = Column(String)
  pronouns = Column(String)
  email = Column(String)
  password = Column(String)
  bio = Column(String)
  img_url = Column(String)

  posts = relationship("PostORM", back_populates="author")
