from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
)

mysql_con= "mysql+mysqlconnector://narendb:Admin123$@narendb.mysql.database.azure.com:3306/narendatabase"

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "User_account"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(30))
    password = Column(String(30))

engine = create_engine(mysql_con, echo=True)
Base.metadata.create_all(engine) 

def createconnection():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except Exception as e:
        print("error in create connection-----", e)

def user_add(mail,passwd):
    try:
        session = createconnection()
        stmt=select(User).where(User.email==mail)
        result = session.execute(stmt).first()
        if result:
            return (f"email: {mail} is alredy present try with other mail")
        else:
            user_data=User(email=mail,password=passwd)
            session.add(user_data)
            session.commit()
            session.close()
            return "User created Succussfully"
    except Exception as e:
        return ("error in creat accout", str(e))

print(user_add("narend@gmail.com","Rowdy@143"))


