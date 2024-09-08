from fastapi import APIRouter, HTTPException, Response, status
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.users.auth import get_password_hash, authenticate_user
from app.users.dao import UsersDAO
from app.users.schemas import SUserRegister, SUserAuth
from app.users.dependencies import create_acces_token
import os


script_dir = os.path.dirname(__file__)
router = APIRouter(prefix='/auth', tags=['auth'])

templates_abs_file_path = os.path.join(script_dir, "../templates/")
templates = Jinja2Templates(directory=templates_abs_file_path)


@router.get('/')
def auth_page(request: Request):
    return templates.TemplateResponse(request=request, name="auth.html")


@router.post('/register/')
async def register_user(user_data: SUserRegister) -> dict:
    user = await UsersDAO.find_one_or_none(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует.'
        )
    user_dict = user_data.dict()
    user_dict['password'] = get_password_hash(user_data.password)
    await UsersDAO.add(**user_dict)
    return {'message': 'Вы успешно зарегестрированы!'}


@router.post("/login/")
async def auth_user(response: Response, user_data: SUserAuth):
    check = await authenticate_user(email=user_data.email, password=user_data.password)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')
    access_token = create_acces_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}


@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return templates.TemplateResponse(request=response, name="unauthorized.html")
