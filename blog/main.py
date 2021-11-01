from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas
from . import models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/posts")
async def get_posts(db : Session = Depends(get_db)):
  posts = db.query(models.Post).all()
  return posts

@app.get("/posts/{id}")
async def get_post(id:int, response: Response, db : Session = Depends(get_db)):
  post = db.query(models.Post).filter(models.Post.id == id).first()
  if not post:
    raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
  return post

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create(request: schemas.BlogPost, db : Session = Depends(get_db)):
  new_post = models.Post(body = request.body, likes = 0, published = False, tag = request.tag)
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id:int, request: schemas.BlogPost, db : Session = Depends(get_db)):
  new_post = db.query(models.Post).filter(models.Post.id == id)
  if not new_post.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
  new_post.update(request, synchronize_session=False)
  db.commit()
  return new_post

@app.delete("/posts/{id}")
async def delete_post(id:int, db : Session = Depends(get_db)):
  db.query(models.Post).filter(models.Post.id == id).delete(synchronize_session=False)
  db.commit()
  return {"message": f"Post with id {id} deleted!"}