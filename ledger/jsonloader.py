import json

def jsonloader(path: str):
    data_file = open(path, "r")
    return json.load(data_file)
