from jose import JWTError ,jwt 
from datetime import datetime, timedelta, timezone
from . import schemas,database,models
from fastapi import Depends ,status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

#SECRET_KEY
#ALGORITHM
#Expiration time

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY=settings.secret_key
ALGORITHM =settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data:dict):
     # 1. Make a copy of the data you want to include in the token
    to_encode =data.copy()

     # 2. Set an expiration time for the token 
    expire= datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

     # 3. Add the expiration time to the data
    to_encode.update({"exp": expire})
     # 4. Encode the data as a JWT (JSON Web Token) using a secret key
    encoded_jwt =jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



def verify_access_token(token:str ,credentials_exception):
   
   try:
          # Decode the JWT token
         payload =jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
         # Extract the user ID
         id: str = payload.get("user_id") # must match what you put in create_access_token
         if id is None:
          raise credentials_exception
         
            # Return TokenData object (usually just a simple class with id)
         token_data =schemas.TokenData(id=id)
   except JWTError:
       raise credentials_exception
   return token_data


def get_current_user(token:str = Depends(oauth2_scheme), db:Session=Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})

    token=verify_access_token(token,credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return  user