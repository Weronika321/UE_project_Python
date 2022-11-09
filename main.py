from flask import Flask, render_template, request
from markupsafe import escape
from app.primality_test import primality_test
from app.const import username, password


app = Flask(__name__)

@app.get('/')
def start():
    return render_template('index.html')
    
@app.route('/prime/<number>')
def check_number(number):
    return render_template('prime.html') #f'{primality_test(escape(number))}'
   
@app.route('/image')
def invert_image():
    return render_template('invert_image.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != username or request.form['password'] != password:
            error = 'Invalid username or password. Please try again.'
        else:
            return render_template('time.html')
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)