from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..models import UserORM
from ..hashing import Hash
from ..jwt_auth import create_access_token

def signin (request: OAuth2PasswordRequestForm, db: Session):
  user = db.query(UserORM).filter(UserORM.email == request.username).first()
  
  if not user:
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"User with given email does not exist")
  if not Hash.verify(request.password, user.password):
    raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail=f"Incorrect password")

  access_token = create_access_token(data={"sub":user.email})

  return {"access_token": access_token, "token_type": "bearer"}