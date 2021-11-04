from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from .database import Base
from sqlalchemy.orm import relationship

friends_table = Table('friends', Base.metadata,
    Column('friends_id', Integer, primary_key=True),
    Column('user1_id', Integer, ForeignKey('users.id')),
    Column('user2_id', Integer, ForeignKey('users.id'))
)

class PostORM(Base):
  __tablename__ = "posts"
  id = Column(Integer, primary_key=True, index=True)
  body = Column(String)
  published = Column(Boolean)
  likes = Column(Integer)
  tag = Column(String)
  author_id = Column(Integer, ForeignKey("users.id"))
  
  author = relationship("UserORM", back_populates="posts", foreign_keys=[author_id], uselist=False)
  comments = relationship("CommentORM", back_populates="post")

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
  comments = relationship("CommentORM", back_populates="author")
  friends = relationship("UserORM", secondary=friends_table, primaryjoin = id == friends_table.c.user1_id, secondaryjoin = id == friends_table.c.user2_id)

class CommentORM(Base):
  __tablename__ = "comments"
  id = Column(Integer, primary_key=True, index=True)
  body = Column(String)
  comment_type = Column(String)
  post_id = Column(Integer, ForeignKey("posts.id"))
  author_id = Column(Integer, ForeignKey("users.id"))

  post = relationship("PostORM", back_populates="comments")
  author = relationship("UserORM", back_populates="comments")

