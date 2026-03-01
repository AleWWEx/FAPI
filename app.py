from fastapi import FastAPI, FileResponse, HTTPException
from models import User, UserAge, Feedback, CalcInput
from typing import List

app = FastAPI()

feedbacks_storage: List[Feedback] = []

#Задание 1.1
@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

#Задание 1.2
@app.get("/html")
async def read_html():
    return FileResponse('index.html')


#Задание 1.3
@app.post("/calculate")
async def calculate(calc: CalcInput):
    result = calc.num1 + calc.num2
    return {"result": result}

#Задание 1.4
@app.get("/users")
async def get_user():
    user = User(name="Ваше Имя и Фамилия", id=1)
    return user

# --- Задание 1.5 ---
@app.post("/user")
async def check_adult(user: UserAge):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

# --- Задание 2.1 и 2.2 ---
@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    feedbacks_storage.append(feedback)
    
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}