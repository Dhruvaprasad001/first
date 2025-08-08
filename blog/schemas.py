from pydantic import BaseModel
from typing import Optional , List

class Blog(BaseModel):
    title: str 
    body: str 
    class Config:   
        orm_mode = True

class User(BaseModel):
    name: str
    username : str
    password : str
    class Config:
        orm_mode = True
    
class ShowUser(BaseModel):
    name:str
    username: str   
    blogs: List[Blog] = []
    class Config:   
        orm_mode = True

class ShowBlog(BaseModel):
    title:str
    body:str
    author:ShowUser
    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username: str | None
    
class LoginRequest(BaseModel):
    username: str
    password: str