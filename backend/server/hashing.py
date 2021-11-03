from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
  def bcrypt(password: str):
    return password_context.hash(password)
  
  def verify(password_in: str, real_password: str):
    return password_context.verify(password_in, real_password)