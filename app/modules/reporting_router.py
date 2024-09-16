from fastapi import APIRouter, HTTPException, Response, status
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.modules.dao import ClientsDAO, NewTradingDAO, ComissionTradingDAO, ScrapDAO, ExpertiseDAO, ServiceDAO
import app.modules.models as BaseModels
import os
from time import strftime


script_dir = os.path.dirname(__file__)
router = APIRouter(prefix='/reporting', tags=['reporting'])

templates_abs_file_path = os.path.join(script_dir, "../templates/")
templates = Jinja2Templates(directory=templates_abs_file_path)


@router.get('')
async def reporting_page(request: Request):
    return templates.TemplateResponse(request=request, name='reporting.html')


@router.get('/report')
async def getting_report(request: Request):
    return templates. TemplateResponse(request=request, name='reporttables.html')