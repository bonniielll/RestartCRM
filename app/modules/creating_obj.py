from fastapi import APIRouter, HTTPException, Response, status
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.modules.models import Clients

import os


script_dir = os.path.dirname(__file__)
router = APIRouter(prefix='/new', tags=['adding'])

templates_abs_file_path = os.path.join(script_dir, "../templates/")
templates = Jinja2Templates(directory=templates_abs_file_path)


@router.get('/clientadd')
async def adding_data(request: Request):
    return templates.TemplateResponse(request=request, name='addnew.html')


@router.get('/clientadd/newclient')
async def adding_data(request: Request):
    return templates.TemplateResponse(request=request, name='addnew.html')
