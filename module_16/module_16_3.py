# используем библиотеку, для работы с веб интерфейсами
from fastapi import FastAPI, Path
from typing import Annotated

# пишем backend интерфейс

# инициализация приложения
app = FastAPI()

users_db = {'1': 'Имя: Example, возраст: 18'}





@app.get('/users')
async def get_users() -> dict:
    return users_db


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=15, description='Enter username', example='UrbanUser')], 
                      age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='24')]) -> str:
    current_index = str(int(max(users_db, key=int)) +1)
    users_db[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {username} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(min_length=1, max_length=100, description='Enter id', example='15')], 
                      username: Annotated[str, Path(min_length=5, max_length=15, description='Enter username', example='UrbanUser')], 
                      age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='24')]) -> str:
    new_user = f'Имя: {username}, возраст: {age}'
    users_db[user_id] = new_user
    return f'The user {user_id} is registered'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(min_length=1, max_length=100, description='Enter id', example='15')]) -> str:
    users_db.pop(user_id)
    return f'user with {user_id} was deleted'





# как запустить приложение? 
# пишем в терминале:
# python3 -m uvicorn main:app и энтер
# uvicorn your_filename:app --reload
# uvicorn module_16.module_16_2:app --reload

# Как перейти на страницу с документацией этой страницы?
# в адресной строке добавить
# /docs







