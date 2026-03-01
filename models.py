from fastapi import FastAPI, FileResponse, HTTPException
from models import User, UserAge, Feedback, CalcInput
from typing import List

app = FastAPI()
#Задание 2.1
feedbacks_storage: List[Feedback] = []

#Задание 1.1
@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

#Задание 1.2
@app.get("/html")
async def read_html():
    return FileResponse('index.html')