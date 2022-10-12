from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse, HTMLResponse
import os
import datetime
from primality_test import primality_test
from invert_colors import invert_colors
from authentication import get_current_username


app = FastAPI()


@app.get("/prime/{number}", response_class=HTMLResponse)
def check_number(number):
    html_content = f"""
    <html>
        <body>
            <h1>{primality_test(number)}</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
    

@app.get("/picture/{filename}", response_class=FileResponse)
def invert_image(filename):
    img = invert_colors(os.path.abspath(filename))
    img.save("image.jpg")
    return os.path.abspath("image.jpg")


@app.get("/auth")
def read_current_user(username: str = Depends(get_current_username)):
    time = datetime.datetime.now().strftime("%H:%M")
    html_content = f"""
    <html>
        <body>
            <h1>Aktualna godzina: {time}</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
