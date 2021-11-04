from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db 
from ..controllers import post
from ..schemas import User, ShowBlogPost, BlogPost
from ..jwt_auth import get_current_user

router = APIRouter(prefix="/posts",tags=["Posts"])

@router.get("/", response_model = List[ShowBlogPost])
async def get_posts(db : Session = Depends(get_db)):
  return post.index(db)

@router.get("/{id}", response_model = ShowBlogPost)
async def get_post(id:int, db : Session = Depends(get_db)):
  return post.show(id, db)

@router.post("/", response_model = ShowBlogPost, status_code=status.HTTP_201_CREATED)
async def create_post(request: BlogPost, db : Session = Depends(get_db), user: User = Depends(get_current_user)):
  return post.create(request, db, user)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id:int, request: BlogPost, db : Session = Depends(get_db), user: User = Depends(get_current_user)):
  return post.update(id, request, db)

@router.delete("/{id}")
async def delete_post(id:int, db : Session = Depends(get_db), user: User = Depends(get_current_user)):
  return post.delete(id, db)