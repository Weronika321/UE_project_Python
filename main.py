import os
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from primality_test import primality_test
from invert_colors import invert_colors

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


