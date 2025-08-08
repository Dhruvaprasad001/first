from fastapi import APIRouter
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, model, hashing
from ..database import engine, SessionLocal
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    tags=["Blogs"],
    prefix="/blog"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=List[schemas.ShowBlog], status_code=status.HTTP_200_OK )
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

@router.post("", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    request.user_id = current_user.id  # Add this line
    return blog.create(db,request)

@router.get("/{id}", response_model=schemas.ShowBlog, status_code=status.HTTP_200_OK)
def get_unique(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_by_id(db, id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.remove(db,id)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Blog)
def updating(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(db,id, request)
