# from flask import Flask
# from flask_restful import Api
# from markupsafe import escape
# from flask import Flask, render_template, redirect, url_for, request



# from app.primality_test import primality_test


# app = Flask(__name__)
# api = Api(app)

# # @app.get('/')
# # def start(): # https://project-ue.herokuapp.com/
# #     return ''
    
# # @app.get('/prime/<number>')
# # def check_number(number): # https://project-ue.herokuapp.com/prime/3
# #     return f'''<h1>{primality_test(escape(number))}</h1>'''
    
# # @app.get('/time')
# # def show_time(): # https://project-ue.herokuapp.com/time
# #     return "time"

# from flask import Flask
# from flask_httpauth import HTTPBasicAuth
# from werkzeug.security import generate_password_hash, check_password_hash

# # app = Flask(__name__)
# auth = HTTPBasicAuth()

# users = {
#     "john": generate_password_hash("hello"),
#     "susan": generate_password_hash("bye")
# }

# @auth.verify_password
# def verify_password(username, password):
#     if username in users and \
#             check_password_hash(users.get(username), password):
#         return username

# @app.route('/')
# @auth.login_required
# def index():
#     return "Hello, {}!".format(auth.current_user())

# if __name__ == "__main__":
#     app.run(debug=False, host="0.0.0.0")


from flask import Flask
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()

if __name__ == '__main__':
    app.run()