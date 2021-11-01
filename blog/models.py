from sqlalchemy import Column, Integer, String, Boolean

from .database import Base

class PostORM(Base):
  __tablename__ = "posts"
  id = Column(Integer, primary_key=True, index=True)
  body = Column(String)
  likes = Column(Integer)
  published = Column(Boolean)
  tag = Column(String)

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
