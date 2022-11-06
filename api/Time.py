from flask_restful import Resource


class Time(Resource):
    def get(self):
        return {"hello": "aut"}
