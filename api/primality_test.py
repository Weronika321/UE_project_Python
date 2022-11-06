from flask_restful import Resource
from app.primality_test import primality_test
from app.html_content import html_content

class PrimalityTest(Resource):
    def get(self):
        number = 9
        return html_content(primality_test(number))
