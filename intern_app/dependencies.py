from fastapi import Depends, HTTPException
<<<<<<< HEAD
from intern_app.config import SECRET_KEY,ALGORITHM
from jose import jwt,JWTError
from sqlalchemy.orm import Session
from .models.user import User
from intern_app.database import get_db
from intern_app.core.security import oauth2_scheme


=======
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session
from .models.user import User
from intern_app.database import get_db


SECRET_KEY = "mysecret987654321key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
<<<<<<< HEAD
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")
        print(payload)
        if email is None:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid credentials"
                )
    except JWTError:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
=======
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    email = payload.get("sub")

>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return user