from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models

def index(db : Session):
  posts = db.query(models.PostORM).all()
  return posts

def show(id:int, db : Session):
  post = db.query(models.PostORM).filter(models.PostORM.id == id).first()
  if not post:
    raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
  return post

def create(request: schemas.BlogPost, db : Session):
  new_post = models.PostORM(body = request.body, likes = 0, published = False, tag = request.tag, author_id=1)
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

def update(id:int, request: schemas.BlogPost, db : Session):
  post = db.query(models.PostORM).filter(models.PostORM.id == id)
  if not post.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
  post.update({"body": request.body, "tag": request.tag, "published": request.published})
  db.commit()
  return {"message": "Updated post!"}

def delete(id:int, db : Session):
  db.query(models.PostORM).filter(models.PostORM.id == id).delete(synchronize_session=False)
  db.commit()
  return {"message": f"Post with id {id} deleted!"}