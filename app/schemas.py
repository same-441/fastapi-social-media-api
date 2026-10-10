from pydantic import BaseModel ,EmailStr , Field
from datetime import datetime
from typing import Optional 
from typing import Annotated #type checker friendly way


class PostBase(BaseModel):
    title:str
    content:str
    published: bool= True

class PostCreate(PostBase):   #extend the postabse model or class
  pass   #pass means all attributes of postbase class inherit


class UserOut(BaseModel):
   id:int
   email:EmailStr
   created_at: datetime
   class Config:  #tells the pydantic model to read the data if it is not a dict
       from_attributes = True   


class Post(PostBase):
   id:int   #the other three attributes are inherited
   created_at: datetime
   owner_id:int
   owner:UserOut

   class Config:  #tells the pydantic model to read the data if it is not a dict
      from_attributes = True 

class PostOut(BaseModel):
      post: Post
      votes:int

      class Config:  #tells the pydantic model to read the data if it is not a dict
         from_attributes = True 


class UserCreate(BaseModel):
   email:EmailStr 
   password:str 

class UserLogin(BaseModel):
   email: EmailStr
   password :str


class Token(BaseModel):
   access_token:str
   token_type:str

class TokenData(BaseModel):
   id: Optional[int] = None

class Vote(BaseModel):
   post_id:int
   dir: Annotated[int, Field(le=1)]