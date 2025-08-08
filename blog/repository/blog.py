from fastapi import APIRouter
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, model, hashing
from ..database import engine, SessionLocal


def get_all(db : Session) :
  blogs = db.query(model.Blog).all()
  return blogs

def create(db:Session , request: schemas.Blog):
    new_blog = model.Blog(
        title=request.title,
        body=request.body,
        user_id=1
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_by_id(db: Session , id: int):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog

def remove(db: Session , id:int):
    blog = db.query(model.Blog).filter(model.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return True

def update(db: Session , id:int, request: schemas.Blog):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update({
        "title": request.title,
        "body": request.body
    })
    db.commit()
    return blog.first()