from flask import Flask, render_template, redirect, url_for, request
from flask_restful import Api
from markupsafe import escape
import pytz, datetime
from app.primality_test import primality_test
from flask_httpauth import HTTPBasicAuth


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
    
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    # if username in users:
    #     return check_password_hash(users.get(username), password)
    return True


# user = 'jane.doe@email.com'
# pw = '1234xyz'
# # users = {
# #     user: generate_password_hash(pw)
# # }

@app.route('/hello')
@auth.login_required
def hello_world():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    # error = None
    # if request.method == 'POST':
    #     if request.form['username'] != 'admin' or request.form['password'] != 'admin':
    #         error = 'Invalid Credentials. Please try again.'
    #     else:
    #         return redirect(url_for('home'))
    return render_template(login.html)
