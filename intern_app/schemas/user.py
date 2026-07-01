from pydantic import BaseModel
from ..schemas.notification import ChannelEnum, StatusEnum
class UserCreate(BaseModel):
    username:str
    email:str
    password:str

class LoginRequest(BaseModel):
    email:str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class NotificationCreate(BaseModel):
    title: str
    message: str
    channel: ChannelEnum
    # user_id: int
    
class NotificationUpdate(BaseModel):
    title: str
    message: str

class NotificationResponse(BaseModel):
    id: int
    title: str
    message: str
    channel: ChannelEnum
    status: StatusEnum

    class Config:
        from_attributes = True

class NotificationStatusUpdate(BaseModel):
    status: StatusEnum