from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..controllers import authentication

router = APIRouter(tags=["Authentication"])

get_db = database.get_db

@router.post("/login", response_model= schemas.BaseUser)
def login(request: schemas.Login, db: Session = Depends(get_db)):
  return authentication.signin(request, db)