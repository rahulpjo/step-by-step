from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session
from cloudinary.uploader import upload
from ..schemas import User
from ..models import UserORM

def update_user_photo(file: UploadFile, db : Session, user: User):
  user_info = db.query(UserORM).filter(UserORM.email == user.username).first()
  if not user_info:
    raise HTTPException(status_code=404, detail=f"User with id {id} not found")
  response = upload(file.file)
  user_info.img_url = response["url"]
  db.commit()
  return {"message": "Picture uploaded successfully!", "url": response["url"] }