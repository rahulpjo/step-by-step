from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import User, ShowUser
from ..database import get_db
from ..controllers import user

router = APIRouter(prefix="/users",tags=["Users"])

@router.get("/{id}", response_model = ShowUser)
def get_user(id:int, db : Session = Depends(get_db)):
  return user.show(id, db)

@router.post("/", response_model = ShowUser)
def create_user(request: User, db : Session = Depends(get_db)):
  return user.create(request, db)
  
