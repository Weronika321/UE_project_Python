from typing import Union

from fastapi import FastAPI

from is_prime import is_prime

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello world!"


@app.get("/prime/{number}")
def check_number(number):
    return is_prime(number)

    # return self.value is int and self.value > 1 and self.value < 9223372036854775807
