from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from ..controllers import photo
from ..database import get_db 
from ..schemas import User
from ..jwt_auth import get_current_user

router = APIRouter(prefix="/files",tags=["Files"])

SAVE_PATH = "../media"


@router.post("/upload")
def upload_picture(file: UploadFile = File(...), db : Session = Depends(get_db), user: User = Depends(get_current_user)):
  return photo.update_user_photo(file, db, user)