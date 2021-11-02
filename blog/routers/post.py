from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..controllers import post

router = APIRouter(prefix="/posts",tags=["Posts"])
get_db = database.get_db

@router.get("/", response_model = List[schemas.ShowBlogPost])
async def get_posts(db : Session = Depends(get_db)):
  return post.index(db)

@router.get("/{id}", response_model = schemas.ShowBlogPost)
async def get_post(id:int, db : Session = Depends(get_db)):
  return post.show(id, db)

@router.post("/", response_model = schemas.ShowBlogPost, status_code=status.HTTP_201_CREATED)
async def create_post(request: schemas.BlogPost, db : Session = Depends(get_db)):
  return post.create(request, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id:int, request: schemas.BlogPost, db : Session = Depends(get_db)):
  return post.update(id, request, db)

@router.delete("/{id}")
async def delete_post(id:int, db : Session = Depends(get_db)):
  return post.delete(id, db)