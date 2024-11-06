from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome() -> str:
    return 'Main page'


@app.get('/user/admin')
async def admin() -> str:
    return 'Вы зашли как админ'

@app.get('/user/{user_id}')
async def sign_up(user_id: int) -> str:
    return f'Вы вошли как пользователь № {user_id}>'

@app.get('/user')
async def news(username: str = 'Name', age: int = -1) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
