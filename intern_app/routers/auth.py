from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User,Notification
<<<<<<< HEAD
from ..schemas.user import NotificationCreate, NotificationUpdate
=======

from ..schemas.user import LoginRequest,NotificationCreate, NotificationUpdate
>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
from intern_app.dependencies import get_current_user
from ..core.security import verify_password,create_access_token,get_password_hash

router= APIRouter()

<<<<<<< HEAD
@router.get("/user")
=======
@router.get("/")
>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
def profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/register")
def register(username:str, email:str, password:str,db:Session=Depends(get_db)):
    hashed_password= get_password_hash(password)

    db_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        "message": "Registered successfully"
    }
    

@router.post("/login")
<<<<<<< HEAD
def login(form_data: OAuth2PasswordRequestForm = Depends(),db:Session= Depends(get_db)):
=======
def login(form_data: OAuth2PasswordRequestForm = Depends() , db:Session= Depends(get_db)):
>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
    db_user= db.query(User).filter(
        User.email == form_data.username
    ).first()
    
<<<<<<< HEAD
    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

=======
    print("User:", db_user)  
    print("Stored Password:", db_user.password)
    print("Entered Password:", form_data.password)

    is_valid = verify_password(form_data.password, db_user.password)
    print("Verify:", is_valid)
>>>>>>> c1d920b4e1198abbfe06cab9643dde77c8dcb4cf
    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid password")
        
    token = create_access_token(
        {"sub": db_user.email}
)

    return {    
        "access_token": token,
        "token_type": "bearer"
}

@router.post("/notifications")
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_notification = Notification(
        title=notification.title,
        message=notification.message,
        user_id=current_user.user_id
    )

    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)

    return {
        "message": "Notification created successfully",
        "data": db_notification
    }

@router.get("/notifications/search")
def search_notifications(
    title: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    notifications = (
        db.query(Notification)
        .filter(
            Notification.user_id == current_user.user_id,
            Notification.title.ilike(f"%{title}%")
        )
        .all()
    )

    return notifications


@router.get("/notifications/{id}")
def get_notification(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    notification = (
        db.query(Notification)
        .filter(
            Notification.id == id,
            Notification.user_id == current_user.user_id
        )
        .first()
    )

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return notification


@router.put("/notifications/{id}")
def update_notification(
    id: int,
    notification: NotificationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_notification = (
        db.query(Notification)
        .filter(
            Notification.id == id,
            Notification.user_id == current_user.user_id
        )
        .first()
    )

    if not db_notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    db_notification.title = notification.title
    db_notification.message = notification.message

    db.commit()
    db.refresh(db_notification)

    return {
        "message": "Notification updated successfully",
        "data": db_notification
    }
@router.delete("/notifications/{id}")
def delete_notification(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_notification = (
        db.query(Notification)
        .filter(
            Notification.id == id,
            Notification.user_id == current_user.user_id
        )
        .first()
    )

    if not db_notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    db.delete(db_notification)
    db.commit()

    return {
        "message": "Notification deleted successfully"
    }
