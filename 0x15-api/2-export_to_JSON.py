#!/usr/bin/python3
"""
API module

"""
import json
import requests
import sys


if __name__ == '__main__':
    _id = sys.argv[1]
    name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + _id).json()['username']

    data = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + _id).json()
    json_output = []

    for i in data:
        json_output.append({_id: [{
                                "task": i.get("title"),
                                "completed": i.get("completed"),
                                "username": name}]})
    with open(_id + ".json", "w") as _file:
        json.dump(json_output, _file)
