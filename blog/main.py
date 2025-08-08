from fastapi import FastAPI
from . import model
from .database import engine, SessionLocal
from .routers import blog , user , authentication

app = FastAPI()


model.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
