from flask import Flask, request
from flask_restful import Api
from api.HelloWorld import HelloWorld
from api.PrimalityTest import PrimalityTest
from api.InvertColors import InvertColors
from api.Time import Time

app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorld, "/")
api.add_resource(PrimalityTest, "/prime")
api.add_resource(InvertColors, "/invert")
api.add_resource(Time, "/time")

@app.route('/index')
def access_param():
    source = request.args.get('source')
    return '''<h1>The source value is: {}</h1>'''.format(source)
# appFlask.run(debug=True, port=5000)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")  # app.run(debug=True)
