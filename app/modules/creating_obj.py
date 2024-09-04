from fastapi import APIRouter, HTTPException, Response, status, Depends
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.modules.schemas import SClientAdding
from app.modules.dao import ClientsDAO

import os


script_dir = os.path.dirname(__file__)
router = APIRouter(prefix='', tags=['adding'])

templates_abs_file_path = os.path.join(script_dir, "../templates/")
templates = Jinja2Templates(directory=templates_abs_file_path)


@router.get('/new')
async def adding_data(request: Request):
    return templates.TemplateResponse(request=request, name='addnew.html')


@router.get('/clientadd')
async def adding_data(request: Request, client_data: SClientAdding):
    exist_client = await ClientsDAO.find_one_or_none(phone_number=client_data.phone_number)
    if exist_client:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Клиент уже существует')
    client_dict = exist_client.dict()
    try:
        await ClientsDAO.add(**client_dict)
    except:
        raise HTTPException(status_code=status.WS_1011_INTERNAL_ERROR,
                            detail='Произошла непредвиденная ошибка')
    finally:
        return templates.TemplateResponse(request=request, name='addnew.html')
