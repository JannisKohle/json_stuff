# Everything with json

import json


def read(file):
    with open(file, "r") as file2:
        return json.load(file2)


def write(file, towrite):
    with open(file, "w") as file2:
        json.dump(towrite, file2)
