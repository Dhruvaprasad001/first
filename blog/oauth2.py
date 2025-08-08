from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import get_db
from . import token
from . import model

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login",
    scopes={"me": "Read information about the current user.", "items": "Read items."},
)

def get_current_user(token_str: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Verify the token and get the username
    username = token.verify_token(token_str, credentials_exception)
    
    # Fetch the user from the database
    user = db.query(model.User).filter(model.User.username == username).first()
    if user is None:
        raise credentials_exception
    
    return user
  
