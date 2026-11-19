from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as SHTTPexception

templates = Jinja2Templates(directory="templates")

app = FastAPI()
#=========================================================================
@app.get('/' , response_class=HTMLResponse)
async def home_page(request : Request):
    return templates.TemplateResponse(request=request , name='home.html')

@app.get('/login' , response_class=HTMLResponse)
async def login_page(request : Request):
    return templates.TemplateResponse(request=request , name = 'login.html')

@app.get('/registration' , response_class=HTMLResponse)
async def reg_page(request : Request):
    return templates.TemplateResponse(request=request , name='reg.html')

#=========================================================================

@app.exception_handler(404)
async def handler_404(request : Request , exception : SHTTPexception):
    return templates.TemplateResponse(
        request=request,
        name="404.html",
        status_code=404
    )

@app.exception_handler(403)
async def handler_403(request : Request , exception: SHTTPexception):
    return templates.TemplateResponse(
        request=request,
        name = '403.html',
        status_code=403
    )