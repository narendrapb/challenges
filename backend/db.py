from sqlalchemy import create_engine,text
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
    VARBINARY,
    Date,
    JSON,
    Text,
    Float,
    UniqueConstraint,
)

def createconnection():
    try:
        engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except Exception as e:
        print("error in create connection-----", e)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "User_account"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30))
    password = Column(String(30))

def user_add(username,passwd):
    pass
