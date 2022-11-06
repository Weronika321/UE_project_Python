from flask import Flask
from flask_restful import Api
from api.HelloWorld import HelloWorld
from api.PrimalityTest import PrimalityTest
from api.InvertColors import InvertColors
from api.Authentication import Authentication

app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorld, "/")
api.add_resource(PrimalityTest, "/prime")
api.add_resource(InvertColors, "/invert")
api.add_resource(Authentication, "/authentication")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")  # app.run(debug=True)
