from flask import Flask, render_template, redirect, url_for, request
from flask_restful import Api
from markupsafe import escape
import pytz, datetime
from app.primality_test import primality_test


app = Flask(__name__)

@app.get('/')
def start():
    return ''
    
@app.route('/prime/<number>')
def check_number(number):
    return f'{primality_test(escape(number))}'
   
@app.route('/image')
def invert_image():
    return "image"
    
@app.route('/time')
def show_time():
    time = datetime.datetime.now(pytz.timezone('Europe/Warsaw')).strftime("%H:%M")
    return f"Godzina logowania: {time}"
