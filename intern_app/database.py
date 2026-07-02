from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from intern_app.config import DATABASE_URL


DATABASE_URL="sqlite:///./notification.db"      

engine= create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)                                              
SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base=declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
