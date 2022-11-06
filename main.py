# from flask import Flask
# from flask_restful import Api
# from markupsafe import escape
# from flask import Flask, render_template, redirect, url_for, request



# from app.primality_test import primality_test


# app = Flask(__name__)
# # api = Api(app)

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
import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
import logging

load_dotenv()
app = Flask(__name__)
client_id = os.getenv('GOOGLE_CLIENT_ID')
client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
app.secret_key = os.getenv('secret_key')

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

blueprint = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    reprompt_consent=True,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    google_data = None
    user_info_endpoint = '/oauth2/v2/userinfo'
    if google.authorized:
        google_data = google.get(user_info_endpoint).json()

    return render_template('index.j2',
                           google_data=google_data,
                           fetch_url=google.base_url + user_info_endpoint)

@app.route('/login')
def login():
    return redirect(url_for('google.login'))

if __name__ == "__main__":
    app.run()