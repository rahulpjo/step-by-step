from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models
from ..hashing import Hash

def signin (request: schemas.Login, db: Session):
  user = db.query(models.UserORM).filter(models.UserORM.email == request.username).first()
  if not user:
    raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"User with given email does not exist")
  if not Hash.verify(request.password, user.password):
    raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail=f"Incorrect password")
  return user