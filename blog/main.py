from fastapi import FastAPI, Depends, status, HTTPException
from typing import List
from . import schemas
from . import models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/posts", response_model = List[schemas.ShowBlogPost])
async def get_posts(db : Session = Depends(get_db)):
  posts = db.query(models.PostORM).all()
  return posts

@app.get("/posts/{id}", response_model = schemas.ShowBlogPost)
async def get_post(id:int, db : Session = Depends(get_db)):
  post = db.query(models.PostORM).filter(models.PostORM.id == id).first()
  if not post:
    raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
  return post

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create(request: schemas.BlogPost, db : Session = Depends(get_db)):
  new_post = models.PostORM(body = request.body, likes = 0, published = False, tag = request.tag)
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id:int, request: schemas.BlogPost, db : Session = Depends(get_db)):
  post = db.query(models.PostORM).filter(models.PostORM.id == id)
  if not post.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
  post.update({"body": request.body, "tag": request.tag, "published": request.published})
  db.commit()
  return {"message": "Updated post!"}

@app.delete("/posts/{id}")
async def delete_post(id:int, db : Session = Depends(get_db)):
  db.query(models.PostORM).filter(models.PostORM.id == id).delete(synchronize_session=False)
  db.commit()
  return {"message": f"Post with id {id} deleted!"}


@app.post("/users", response_model = schemas.ShowUser)
async def create_user(request: schemas.User, db : Session = Depends(get_db)):
  new_user = models.UserORM(request)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user