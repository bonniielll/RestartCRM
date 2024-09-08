from fastapi import APIRouter, HTTPException, Response, status, Depends, Form
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.modules.schemas import SClientAdding, SNewAdding, SComissionAdding, SScrapAdding, SExperiseAdding, SServiceAdding
from app.modules.dao import ClientsDAO, NewTradingDAO
from typing import Annotated

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
    return templates.TemplateResponse(request=client, name='addnew.html')
    

@router.post('/tradeadd')
async def adding_new_trades(request: Request, trade_data: SNewAdding):
    trade = await NewTradingDAO.find_one_or_none(client=trade_data.client)
    trade_dict = trade.dict()
    await NewTradingDAO.add(**trade_dict)
    return templates.TemplateResponse(request=request, name='addnew.html')
    
