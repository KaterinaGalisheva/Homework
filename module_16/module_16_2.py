# используем библиотеку, для работы с веб интерфейсами
from fastapi import FastAPI
from fastapi import Path 
from typing import Annotated

# инициализация приложения
app = FastAPI()



# маршрут к страницам пользователей
@app.get("/user/{user_id}")
async def user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# маршрут к страницам пользователей
@app.get("/user/{username}/{age}")
async def some_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')], age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


# как запустить приложение? 
# пишем в терминале:
# python3 -m uvicorn main:app и энтер
# uvicorn your_filename:app --reload
# uvicorn module_16.module_16_2:app --reload

# Как перейти на страницу с документацией этой страницы?
# в адресной строке добавить
# /docs

