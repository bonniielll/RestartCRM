from fastapi import APIRouter, HTTPException, Response, status
from app.users.auth import get_password_hash, authenticate_user
from app.users.dao import UsersDAO
from app.users.schemas import SUserRegister, SUserAuth
from app.users.dependencies import create_acces_token

router = APIRouter(prefix='/auth', tags=['auth'])


@router.get('/')
def auth_page():
    return {'qqqqqq': 'qweqwe'}


@router.post('/register/')
async def register_user(user_data: SUserRegister) -> dict:
    user = await UsersDAO.find_one_or_none(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует.'
        )
    user_dict = user.data.dict()
    user_dict['password'] = get_password_hash(user.data.password)
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
