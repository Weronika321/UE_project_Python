import json


def list_to_json(list_of_elements: list) -> str:
    return json.dumps([element.__dict__() for element in list_of_elements])
