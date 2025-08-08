from fastapi import APIRouter
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, model, hashing
from ..database import engine, SessionLocal

def create(db: Session , request: schemas.User):       
    new_user = model.User(
        name=request.name,
        username=request.username,
        password=hashing.Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_all(db:Session):
    return db.query(model.User).all()

def get_by_id(db:Session ,id:int  ):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return user

    