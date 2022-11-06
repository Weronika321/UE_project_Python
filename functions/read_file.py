from io import TextIOWrapper


def read_file(filename: str) -> TextIOWrapper:
    file = open(filename, "r", newline="\n", encoding="utf-8")
    return file
