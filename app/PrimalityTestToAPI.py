import math
from flask_restful import Resource


class PrimalityTestToAPI(Resource):
    def get(self, number):
        try:
            number = int(number)
        except ValueError:
            return "Podano niepoprawne dane"
        
        if number <= 1 or number > 9223372036854775807:
            return "Podano niepoprawne dane"

        for i in (range(2, int(math.sqrt(number)))):
            if number % i == 0:
                return f"{number} nie jest liczbą pierwszą"

        return f"{number} jest liczbą pierwszą"