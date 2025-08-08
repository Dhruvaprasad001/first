from fastapi import APIRouter
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, model, hashing
from ..database import engine, SessionLocal
from ..repository import user
from ..oauth2 import get_current_user

router = APIRouter(
    tags=["User"],
    prefix="/user"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", status_code=status.HTTP_201_CREATED , response_model=schemas.User  )
def create_user(request: schemas.User, db: Session = Depends(get_db) , current_user: schemas.User = Depends(get_current_user)):
    return user.create(db, request)

@router.get("" , response_model=List[schemas.User], status_code=status.HTTP_200_OK )
def get_all_user(db : Session = Depends(get_db) , current_user: schemas.User = Depends(get_current_user)):
    return user.get_all(db)

@router.get("/{id}" , response_model=schemas.ShowUser, status_code=status.HTTP_200_OK )
def get_user(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user.get_by_id(db,id)