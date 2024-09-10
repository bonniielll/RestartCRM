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
router = APIRouter(prefix='', tags=['main'])

templates_abs_file_path = os.path.join(script_dir, "../templates/")
templates = Jinja2Templates(directory=templates_abs_file_path)


@router.get('/clients')
async def clients_base(request: Request):
    clients_data = await ClientsDAO.find_all()
    keys = BaseModels.Clients.__table__.columns.keys()
    data = list()
    column_names = ['Айди', 'Номер телефона', 'ФИО', 'Комментарий', 
                    'Количество взаимодействий', 'Сумма прибыли', 'Сумма выплат', 
                    'Первое взаимодействие', 'Последнее взаимодействие',]
    for n, i in enumerate(clients_data):
        columns = list()
        for row in keys:
            date = getattr(clients_data[n], row)
            try:
                date = date.strftime('%d.%m.%Y %Hч:%Mм')
            except:
                columns.append(getattr(clients_data[n], row))
            else:
                columns.append(date)
        data.append(columns)
    return templates.TemplateResponse(request=request, name='trading.html', context={"data": data, "column_names": column_names})


@router.get('/newt')
async def new_trading(request: Request):
    trades_data = await NewTradingDAO.find_all()
    keys = BaseModels.NewTrading.__table__.columns.keys()
    data = list()
    column_names = ['Номер', 'Магазин', 'Номер клиента', 'АКБ', 'Цена АКБ', 'Старый акб',
                    'Цена старого', 'Скидка', 'Сумма', 'Способ оплаты',
                    'Комментарий', 'По счету', 'Данные счета'
                    , 'Дата создания', 'Дата обновления'] 
    for n, i in enumerate(trades_data):
        columns = list()
        for row in keys:
            date = getattr(trades_data[n], row)
            try:
                date = date.strftime('%d.%m.%Y %Hч:%Mм')
            except:
                columns.append(getattr(trades_data[n], row))
            else:
                columns.append(date)
        data.append(columns)
    return templates.TemplateResponse(request=request, name='trading.html', context={"data": data, "column_names": column_names})


@router.get('/comt')
async def comission_trading(request: Request):
    comission_data = await ComissionTradingDAO.find_all()
    keys = BaseModels.ComissionTrading.__table__.columns.keys()
    data = list()
    column_names = ['Айди', 'АКБ(название,код)', 'Гарантия(Мес)', 'Цена', 'Скидка',
                     'Сумма', 'Метод оплаты', 'Клиент(номер)', 'Дата создания', 'Дата обновления']
    for n, i in enumerate(comission_data):
        columns = list()
        for row in keys:
            date = getattr(comission_data[n], row)
            try:
                date = date.strftime('%d.%m.%Y %Hч:%Mм')
            except:
                columns.append(getattr(comission_data[n], row))
            else:
                columns.append(date)
        data.append(columns)
    return templates.TemplateResponse(request=request, name='trading.html', context={"data": data, "column_names": column_names})


@router.get('/scraptrade')
async def scrap_trading(request: Request):
    scrap_data = await ScrapDAO.find_all()
    keys = BaseModels.ScrapTrading.__table__.columns.keys()
    data = list()
    column_names = ['Айди', 'Клиент(номер телефона)', 'Объём АКБ', 'Сумма выплаты', 'Способ оплаты', 
                    'Комментарий', 'Данные для мандарина', 'Ссылка на фото паспорта', 'Дата создания', 'Дата обновления']
    for n, i in enumerate(scrap_data):
        columns = list()
        for row in keys:
            date = getattr(scrap_data[n], row)
            try:
                date = date.strftime('%d.%m.%Y %Hч:%Mм')
            except:
                columns.append(getattr(scrap_data[n], row))
            else:
                columns.append(date)
        data.append(columns)
    return templates.TemplateResponse(request=request, name='trading.html', context={"data": data, "column_names": column_names})


@router.get('/expertise')
async def expertise(request: Request):
    expertise_data = await ExpertiseDAO.find_all()
    keys = BaseModels.Expertise.__table__.columns.keys()
    data = list()
    column_names = ['Айди', 'Название акб', 'Клиент(номер)', 'Когда обнаружили брак', 'Где документы', 'Где акб', 
                    'Комментарий', 'Подменный АКБ', 'Кто принял(имя)', 'Где приняли(точка)', 'Дата создания', 'Дата обновления']
    for n, i in enumerate(expertise_data):
        columns = list()
        for row in keys:
            date = getattr(expertise_data[n], row)
            try:
                date = date.strftime('%d.%m.%Y %Hч:%Mм')
            except:
                columns.append(getattr(expertise_data[n], row))
            else:
                columns.append(date)
        data.append(columns)
    return templates.TemplateResponse(request=request, name='trading.html', context={"data": data, "column_names": column_names})


@router.get('/service')
async def service(request: Request):
    scrap_data = await ServiceDAO.find_all()
    keys = BaseModels.Service.__table__.columns.keys()
    data = list()
    column_names = ['Айди', 'Название АКБ', 'За услуги', 'Комментарий', 'Подменный АКБ', 
                    'Залог за подмен', 'После возврата клиенту', 'Способ оплаты', 'Дата создания', 'Дата обновления']
    for n, i in enumerate(scrap_data):
        columns = list()
        for row in keys:
            date = getattr(scrap_data[n], row)
            try:
                date = date.strftime('%d.%m.%Y %Hч:%Mм')
            except:
                columns.append(getattr(scrap_data[n], row))
            else:
                columns.append(date)
        data.append(columns)
    return templates.TemplateResponse(request=request, name='trading.html', context={"data": data, "column_names": column_names})
