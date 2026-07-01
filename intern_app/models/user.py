from sqlalchemy import Column,Integer,String,ForeignKey
from ..database import Base

class User(Base):
    __tablename__= "users"
    user_id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True)
    email=Column(String,unique=True)
    password=Column(String)
class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    message = Column(String)
    user_id = Column(Integer, ForeignKey("users.user_id"))