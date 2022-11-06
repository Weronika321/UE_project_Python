from flask_restful import Resource
from app.primality_test import primality_test

class PrimalityTest(Resource):
    def get(self):
        number = 9
        return primality_test(number)
