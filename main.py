from http.client import responses
from random import randint
from PIL import Image, ImageChops

import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse

from is_prime import is_prime
from invert_colors import invert_colors

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello world!"


@app.get("/prime/{number}")
def check_number(number):
    return is_prime(number)

@app.get("/invert")
def check_number():
    picture = Image.open("pencils.jpg")
    # picture.show()
    return "obrazek"

    # return self.value is int and self.value > 1 and self.value < 9223372036854775807


@app.get("/picture/{filename}", response_class=FileResponse)
async def read_items(filename):
    img = invert_colors(os.path.abspath(filename))
    img.save("image.jpg")
    return os.path.abspath("image.jpg")
    
# img = invert_colors(os.path.abspath("pobrane.jpg"))
# img.show()
# img = invert_colors(os.path.abspath("pobrane.jpg"))
# print(img.path)
