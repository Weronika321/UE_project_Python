from flask import Flask, request
from flask_restful import Api
from api.HelloWorld import HelloWorld
from api.InvertColors import InvertColors
from api.Time import Time
from app.primality_test import primality_test


app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorld, "/")
api.add_resource(InvertColors, "/invert")
api.add_resource(Time, "/time")

@app.get('/prime')
def access_param(): # https://project-ue.herokuapp.com/prime?number=3
    number = request.args.get('number')
    if number is None:
        return f"Nie podano liczby"
    else:
        return f'''<h1>{primality_test(number)}</h1>'''



if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")  # app.run(debug=True)
