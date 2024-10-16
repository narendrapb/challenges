import os
from dotenv import load_dotenv
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    update,
    delete,
)
load_dotenv()
mysql_con = os.getenv("MYSQL_CONN")

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
        stmt=select(User.email).where(User.email==mail)
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
    finally:
        if session:
            session.close()

def password_change(mail,newpass,oldpass):
    try: 
        session = createconnection()
        stmt=select(User.email).where(User.email==mail)
        result = session.execute(stmt).first()
        if not result:
            return "Enter Valid mail"
        pass_stmt=select(User.email).where(User.email==mail and User.password==oldpass)
        pass_check=session.execute(pass_stmt).first()
        if pass_check:
            update_passwd = update(User).values(password = newpass).where(User.email==mail)
            session.execute(update_passwd)
            session.commit()
            session.close()
            return "Password updated successfully"
        else:
            return "Password is Incorrect Please enter correct password"
    except Exception as e:
        return ("error in Updating Password", str(e))
    finally:
        if session:
            session.close()




