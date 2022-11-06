from flask_restful import Resource
from functions.read_file import read_file
from functions.file_to_list import file_to_list
from functions.list_to_json import list_to_json
from functions.read_JSON import read_JSON


class Tags_to_API(Resource):
    def get(self):
        return read_JSON(
            list_to_json(file_to_list(read_file("data/tags.csv"))[1:])
        )
