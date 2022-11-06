import csv
from io import TextIOWrapper
from classes.Movie import Movie


def file_to_list(file_reader: TextIOWrapper) -> list:
    result = []

    for row in csv.reader(file_reader, delimiter=","):
        result.append(Movie(row[0], row[1], row[2]))

    return result
