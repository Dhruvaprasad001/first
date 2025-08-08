from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, model , token
from ..database import get_db
from ..hashing import Hash
from ..token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["Authentication"],
    prefix="/login",
)

@router.post("")
async def login(request: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    access_token = token.create_access_token(
        data={"sub": user.username}
    )
    
    return { "access_token": access_token, "token_type": "bearer", "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60 }