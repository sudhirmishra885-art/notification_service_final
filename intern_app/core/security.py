from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from jose import jwt
<<<<<<< HEAD

from fastapi.security import OAuth2PasswordBearer

=======
from dotenv import load_dotenv
import os
>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
from intern_app.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
<<<<<<< HEAD
oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "login")
=======
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",30)
)

>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

<<<<<<< HEAD
def get_password_hash(password:str):
    return pwd_context.hash(password)

def verify_password(
        plain_password:str,
        hashed_password:str):
=======
def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(
        plain_password,
        hashed_password):
>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
<<<<<<< HEAD

def create_access_token(data:dict,expires_delta:timedelta|None=None):
      
=======
SECRET_KEY = "mysecret987654321key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
def create_access_token(data:dict,expires_delta:timedelta|None=None):
>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
        to_encode = data.copy()
        if expires_delta:
             expire = datetime.now(timezone.utc) + expires_delta
        else:
             expire= datetime.now(timezone.utc) + timedelta(
                  minutes= ACCESS_TOKEN_EXPIRE_MINUTES
             )

        to_encode.update({"exp":expire})
        encoded_jwt=jwt.encode(
             to_encode,
             SECRET_KEY,
             algorithm= ALGORITHM
        )
        return encoded_jwt
<<<<<<< HEAD
=======

>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
