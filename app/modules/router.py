from fastapi import APIRouter, HTTPException, Response, status
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.modules.dao import ClientsDAO
import app.modules.models as BaseModels
import os


script_dir = os.path.dirname(__file__)
router = APIRouter(prefix='', tags=['main'])

templates_abs_file_path = os.path.join(script_dir, "../templates/")
templates = Jinja2Templates(directory=templates_abs_file_path)


@router.get('/clients')
async def clients_base(request: Request):
    clients_data = await ClientsDAO.find_all()
    print(clients_data)
    return templates.TemplateResponse(request=request, name='base.html')


@router.get('/newt')
async def new_trading(request: Request):
    return templates.TemplateResponse(request=request, name='trading.html')


@router.get('/comt')
async def comission_trading(request: Request):
    return templates.TemplateResponse(request=request, name='trading.html')


@router.get('/scraptrade')
async def scrap_trading(request: Request):
    return templates.TemplateResponse(request=request, name='trading.html')


@router.get('/expertise')
async def expertise(request: Request):
    return templates.TemplateResponse(request=request, name='trading.html')

