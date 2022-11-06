from flask_restful import Resource, reqparse


class PrimalityTestToAPI(Resource):
    def post(self, number):
        return f"{number}"

        # return parser.parse_args()