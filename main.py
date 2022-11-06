from flask import Flask
from flask_restful import Api
from markupsafe import escape


from app.primality_test import primality_test


app = Flask(__name__)
api = Api(app)

@app.route('/')
def access_param(): # https://project-ue.herokuapp.com/
    return ''
    
@app.route('/prime/<number>')
def access_param(number): # https://project-ue.herokuapp.com/prime/3
    return f'''<h1>{primality_test(escape(number))}</h1>'''
    
@app.route('/time')
def access_param(): # https://project-ue.herokuapp.com/time
    return f"time"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
