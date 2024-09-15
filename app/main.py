from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.users.router import router as router_users
from app.modules.router import router as router_modules
from app.modules.creating_obj import router as router_objects
from app.modules.reporting_router import router as router_reports
import os


app = FastAPI()

script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
templates_abs_file_path = os.path.join(script_dir, "templates/")
app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")

templates = Jinja2Templates(directory=templates_abs_file_path)


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse(request=request, name="base.html")


app.include_router(router_users)
app.include_router(router_modules)
app.include_router(router_objects)
app.include_router(router_reports)
