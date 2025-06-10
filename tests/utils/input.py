import json


def read_json_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
