from flask import Flask, request
from flask_restful import Api

from app.primality_test import primality_test


app = Flask(__name__)
api = Api(app)

@app.get('/')
def access_param(): # https://project-ue.herokuapp.com/
    return ''
    
@app.get('/prime')
def access_param(): # https://project-ue.herokuapp.com/prime?number=3
    number = request.args.get('number')
    if number is None:
        return f"Nie podano liczby"
    else:
        return f'''<h1>{primality_test(number)}</h1>'''
    
@app.get('/time')
def access_param(): # https://project-ue.herokuapp.com/time
    return f"time"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
