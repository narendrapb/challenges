from fastapi import FastAPI
from db import *

app=FastAPI()

def get_app_description():
  return (" i am Narendra Trying to build an application that having Frontend and Backend and Database")

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
