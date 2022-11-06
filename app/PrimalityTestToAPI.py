from flask_restful import Resource, reqparse


class PrimalityTestToAPI(Resource):
    def get(self, number):
        return f"{number}"

        # return parser.parse_args()