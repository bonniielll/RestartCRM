from fastapi import APIRouter, HTTPException, Response, status, Depends, Form
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.modules.schemas import SClientAdding, SNewAdding, SComissionAdding, SScrapAdding, SExperiseAdding, SServiceAdding
from app.modules.dao import ClientsDAO, NewTradingDAO, ComissionTradingDAO
from typing import Annotated
from app.users.dependencies import get_current_user
import os


script_dir = os.path.dirname(__file__)
router = APIRouter(prefix='', tags=['adding'])

templates_abs_file_path = os.path.join(script_dir, "../templates/")
templates = Jinja2Templates(directory=templates_abs_file_path)


@router.get('/new')
async def adding_data(request: Request):
    # TODO: сверстать страницу с карточками добавления данных и дописать в schemas, creating_obj
    return templates.TemplateResponse(request=request, name='addnew.html')


@router.post('/clientadd')
async def adding_clients(client: SClientAdding) -> dict:
    user = await ClientsDAO.find_one_or_none(phone_number=client.phone_number)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Клиент уже существует'
        )
    client_dict = client.dict()
    await ClientsDAO.add(**client_dict)
    return {'message': 'Клиент добавлен!'}
    

@router.post('/tradeadd')
async def adding_new_trades(trade_data: SNewAdding) -> dict:
    trade_dict = trade_data.dict()
    await NewTradingDAO.add(**trade_dict)
    return {'message': 'Продажа нового акб добавлена!'}


@router.post('/comtradeadd')
async def adding_comission_trades(trade_data: SComissionAdding) -> dict:
    trade_dict = trade_data.dict()
    await ComissionTradingDAO.add(**trade_dict)
    return {'message': 'Продажа РАБ Б/У добавлена!'}
