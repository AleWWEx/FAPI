from pyndatic import BaseModel, Field, field_validator
from typing import Optional

class User (BaseModel):
    name: str
    id: int

class CalcInput(BaseModel):
    num1: float
    num2: float

class UserAge(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str = Field(..., min_lenght=2, max_lenght=50, description="Имя от 2 до 50 символов")
    massage str = Field(..., min_lenght=10, max_lenght=500, description="Сообщение от 10 до 500 символов")

    @field_validator('message')
    @classmethod
    def check_banned_words(cls, v):
        banned_words = ["кринж", "рофл", "вайб"]
        v_lower = v.lower()
        for word in banned_words:
            if word in v_lower:
                raise ValueError("Использование недопустимых слов")
        return v