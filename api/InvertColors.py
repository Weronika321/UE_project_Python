from flask_restful import Resource


class InvertColors(Resource):
    def get(self):
        return {"hello": "color"}
