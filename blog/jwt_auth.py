import os
from dotenv import load_dotenv
from jose import JWTError, jwt
from pydantic import BaseModel

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  username: str