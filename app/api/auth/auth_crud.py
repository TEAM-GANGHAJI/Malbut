#-from jose import jwt, JWTError
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from database.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60 * 30
ACCESS_SECRET_KEY = "secret"

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )
  
#   try:
#     payload = jwt.decode(token, ACCESS_SECRET_KEY, algorithms=[ALGORITHM])
#     user_id: str = payload["sub"]
#     if not user_id:
#       raise credentials_exception
    
#   except JWTError:
#     raise credentials_exception
  
#   user = await user_crud.get(
#      db, 
#      user_id=user_id
#     )  
#   if not user:
#     raise credentials_exception

  return "user"
