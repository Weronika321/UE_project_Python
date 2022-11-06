from flask import Flask
from flask_restful import Api
from markupsafe import escape
from flask import Flask, render_template, redirect, url_for, request
import tzlocal
import datetime
from app.primality_test import primality_test



app = Flask(__name__)
# api = Api(app)

@app.get('/')
def start(): # https://project-ue.herokuapp.com/
    return ''
    
@app.get('/prime/<number>')
def check_number(number): # https://project-ue.herokuapp.com/prime/3
    return f'''<h1>{primality_test(escape(number))}</h1>'''
   
@app.get('/image')
def invert_image(): # https://project-ue.herokuapp.com/time
    return "time" 
    
@app.get('/time')
def show_time(): # https://project-ue.herokuapp.com/time
    time = tzlocal.get_localzone().localize(datetime.datetime.now()).strftime("%H:%M")
    return f"Godzina logowania: {time}"


# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello'
# @app.route('/hello')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     print('Starting app')
#     app.run(host='0.0.0.0', debug=True, port=8080)
    
# from flask_httpauth import HTTPBasicAuth
# auth = HTTPBasicAuth()

# @auth.verify_password
# def verify_password(username, password):
#     # if username in users:
#     #     return check_password_hash(users.get(username), password)
#     return True


# user = 'jane.doe@email.com'
# pw = '1234xyz'
# # users = {
# #     user: generate_password_hash(pw)
# # }

# @app.route('/hello')
# @auth.login_required
# def hello_world():
#     return 'Hello, World!'