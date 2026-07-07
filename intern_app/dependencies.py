from fastapi import Depends, HTTPException
from intern_app.config import SECRET_KEY,ALGORITHM
from jose import jwt,JWTError
from sqlalchemy.orm import Session
from .models.user import User
from intern_app.database import get_db
from intern_app.core.security import oauth2_scheme


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
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
    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return user