from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
import os
import datetime
from io import BytesIO

from app.primality_test import primality_test
from app.invert_colors import invert_colors
from app.authentication import get_current_username
import app.const
from app.html_content import html_content


app = FastAPI()

@app.get("/")
def start():
    return ""

@app.get("/prime/{number}", response_class=HTMLResponse)
def check_number(number):
    html = html_content(primality_test(number))
    return HTMLResponse(content=html, status_code=200)


@app.get("/picture/{filename}", response_class=FileResponse)
def invert_image(filename):
    img = invert_colors(os.path.abspath(filename))
    img.save(app.const.img_name)
    return os.path.abspath(app.const.img_name)


@app.get("/auth")
def read_current_user(username: str = Depends(get_current_username)):
    time = datetime.datetime.now().strftime("%H:%M")
    html = html_content(f"Godzina logowania: {time}")
    return HTMLResponse(content=html, status_code=200)


# docker run -d --name container -p 80:80 image
# docker build -t image .
