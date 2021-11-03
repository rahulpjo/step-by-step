from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..schemas import User
from ..models import UserORM

def create(request: User, db : Session):
  
  new_user = UserORM(
    first_name=request.first_name, 
    last_name=request.last_name, 
    pronouns=request.pronouns, 
    email=request.email, 
    password=Hash.bcrypt(request.password), 
    bio=request.bio, 
    img_url=request.img_url)

  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def show(id:int, db : Session):
  user = db.query(UserORM).filter(UserORM.id == id).first()
  if not user:
    raise HTTPException(status_code=404, detail=f"User with id {id} not found")
  return user
