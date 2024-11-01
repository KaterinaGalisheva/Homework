'''Задача "Модель пользователя":
Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
id - номер пользователя (int)
username - имя пользователя (str)
age - возраст пользователя (int)

Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:
Добавляет в список users объект User.
id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
Все остальные параметры объекта User - переданные в функцию username и age соответственно.
В конце возвращает созданного пользователя.
put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
delete запрос по маршруту '/user/{user_id}', теперь:
Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.'''





'''Модели данных Pydantic'''

from typing import Annotated, List
from fastapi import Body, FastAPI, HTTPException, Path
from pydantic import BaseModel

app = FastAPI()

users_db = []

class User(BaseModel):
    user_id: int 
    username: str
    age: int


@app.get('/users')
def get_users() -> list:
    return users_db


@app.post('/user/{username}/{age}')
def create_user(username: Annotated[str, Path(min_length=5, max_length=15, description='Enter username', example='UrbanUser')], 
                age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='24')]) -> User:
    if not users_db:
        user_id = 1
    else:
        user_id = len(users_db)+1

    new_user = User(user_id=user_id, username=username, age=age)
    users_db.append(new_user)
    print(f'User {user_id} with name: {username} and age: {age} was registered')
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter id', example='15')], 
                      username: Annotated[str, Path(min_length=5, max_length=15, description='Enter username', example='UrbanUser')], 
                      age: Annotated[int, Path(ge=18, le=100, description='Enter age', example='24')]) -> User:
    for ex_user in users_db:
        if ex_user.user_id == user_id:
            ex_user.username = username
            ex_user.age = age
            return ex_user
    raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{user_id}')
def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter id', example='15')]) -> str:
    try:
        users_db.pop(user_id)
        return f'user with {user_id} was deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')






# как запустить приложение? 
# пишем в терминале:
# python3 -m uvicorn main:app и энтер
# uvicorn your_filename:app --reload
# uvicorn module_16.module_16_4:app --reload

# Как перейти на страницу с документацией этой страницы?
# в адресной строке добавить
# /docs

