from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from cloudinary.uploader import upload
from ..database import get_db 
from ..schemas import User
from ..models import UserORM
from ..oauth2 import get_current_user

router = APIRouter(prefix="/files",tags=["Files"])

SAVE_PATH = "../media"


@router.post("/upload")
def upload_picture(file: UploadFile = File(...), db : Session = Depends(get_db), user: User = Depends(get_current_user)):
  user_info = db.query(UserORM).filter(UserORM.email == user.username).first()
  if not user_info:
    raise HTTPException(status_code=404, detail=f"User with id {id} not found")
  response = upload(file.file)
  user_info.img_url = response["url"]
  db.commit()
  return {"message": "Picture uploaded successfully!"}