from flask import Flask
from flask_restful import Api
# from markupsafe import escape
# from flask import Flask, render_template, redirect, url_for, request



# from app.primality_test import primality_test


app = Flask(__name__)
api = Api(app)

@app.route('/')
def access_param(): # https://project-ue.herokuapp.com/
    return ''
    
# @app.route('/prime/<number>')
# def access_param(number): # https://project-ue.herokuapp.com/prime/3
#     return f'''<h1>{primality_test(escape(number))}</h1>'''
    
@app.route('/time')
def access_param(): # https://project-ue.herokuapp.com/time
    return f"time"

# Route for handling the login page logic
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
