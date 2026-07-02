from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone
from jose import jwt
from dotenv import load_dotenv
import os
from intern_app.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",30)
)

pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(
        plain_password,
        hashed_password):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
SECRET_KEY = "mysecret987654321key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
def create_access_token(data:dict,expires_delta:timedelta|None=None):
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

