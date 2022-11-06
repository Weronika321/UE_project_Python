from flask import Flask, render_template, request
from markupsafe import escape
from app.primality_test import primality_test
from app.validation import validate


app = Flask(__name__)

@app.get('/')
def start():
    return ''
    
@app.route('/prime/<number>')
def check_number(number):
    return f'{primality_test(escape(number))}'
   
@app.route('/image')
def invert_image():
    return render_template('invert.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if validate(request.form['username'], request.form['password']):
            error = 'Invalid username or password. Please try again.'
        else:
            return render_template('time.html')
    return render_template('login.html', error=error)

app.run(debug=True)

