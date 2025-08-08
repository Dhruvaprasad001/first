from datetime import datetime, timedelta
from jose import jwt
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import model
from .database import get_db
from . import schemas

SECRET_KEY="sdfsdfwsd123123"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
 
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow()  + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
   try:
         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
         username: str = payload.get("sub")
         if username is None:
              raise credentials_exception
         # Return the username instead of token_data
         return username
   except jwt.JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
  