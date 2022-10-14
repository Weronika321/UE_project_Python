from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
import os
import datetime
from io import BytesIO

from primality_test import primality_test
from invert_colors import invert_colors
from authentication import get_current_username
import const
from html_content import html_content


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
    img.save("image.jpg")
    return os.path.abspath("image.jpg")



@app.get("/auth")
def read_current_user(username: str = Depends(get_current_username)):
    time = datetime.datetime.now().strftime("%H:%M")
    html = html_content(f"Godzina logowania: {time}")
    return HTMLResponse(content=html, status_code=200)
