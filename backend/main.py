from fastapi import FastAPI
from db import createconnection,user_add

app=FastAPI()

def get_app_description():
  return (" i am Narendra Trying to build an application that having Frontend and Backend and Database")

@app.get("/")
async def get_home_page():
  return get_app_description()

@app.post("/create_account")
async def login_web_account(username: str,password: str):
  try:
    session = createconnection()
  except Exception as e:
        print("error in creat accout", str(e))

  return get_app_description()