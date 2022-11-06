from flask_restful import Resource, reqparse


class PrimalityTestToAPI(Resource):
    def get(self, number):
        parser = reqparse.RequestParser()
        parser.add_argument('key1', type=str)
        parser.add_argument('key2', type=str)

        return parser.parse_args()