from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import *

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production to your front-end origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_app_description():
  return (" i am Narendra Trying to build an application that having Frontend, Backend and Database")

@app.get("/")
async def get_home_page():
  return get_app_description()

@app.post("/create_account")
async def login_web_account(mail: str,password: str):
  return user_add(mail,password)

@app.post("/passwd_change")
async def login_web_account(mail: str,passwd: str,new_passwd: str):
  if passwd==new_passwd:
    return "Old Password and New Password cannot be same Please Enter Different Password"
  else:
    return password_change(mail,new_passwd,passwd)

@app.post("/delete_account")
async def delete_account(mail:str,passwd: str):
  try:
    session = createconnection()
    stmt=select(User).where(User.email==mail)
    user = session.execute(stmt).scalar_one_or_none()
    if not user:
      return "Enter Valid mail"
    if user.password != passwd:
      return "Incorrect password"
        # Delete the account
    delete_acc = delete(User).where(User.email == mail)
    session.execute(delete_acc)
    session.commit()
    return "Account deleted successfully" 
  except Exception as e:
    return ("error in Updating Password", str(e))
  finally:
        if session:
            session.close()

@app.post("/login_account")
async def login_account(mail: str, passwd: str):
    try:
        session = createconnection()

        # Check if the user exists
        stmt = select(User).where(User.email == mail)
        user = session.execute(stmt).scalar_one_or_none()

        if not user:
            return "Invalid email, account not found"

        # Check if the password matches
        if user.password != passwd:
            return "Incorrect password"

        return "Login successful"
    
    except Exception as e:
        return ("Error in login", str(e))
    
    finally:
        if session:
            session.close()

