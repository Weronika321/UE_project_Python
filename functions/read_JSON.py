from io import TextIOWrapper
import json


def read_JSON(filename: str) -> TextIOWrapper:

    return json.loads(filename)
