from fastapi import FastAPI, HTTPException , Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get('/' , response_class=HTMLResponse)
async def home_page(request : Request):
    return templates.TemplateResponse(request=request , name='home.html')

@app.get('/login' , response_class=HTMLResponse)
async def login_page(request : Request):
    return templates.TemplateResponse(request=request , name = 'login.html')

@app.get('/reg' , response_class=HTMLResponse)
async def reg_page(request : Request):
    return templates.TemplateResponse(request=request , name='reg.html')