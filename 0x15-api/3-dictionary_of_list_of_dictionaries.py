#!/usr/bin/python3
"""
API module

"""
import json
import requests
import sys


if __name__ == '__main__':
    _url = 'https://jsonplaceholder.typicode.com'
    db = {}
    for user in requests.get(_url + '/users').json():
        _id = str(user.get('id'))
        name = requests.get(
            _url + '/users/' + _id).json()['username']
        data = requests.get(_url + '/todos?userId=' + _id).json()
        lis = []
        for task in data:
            lis.append({
                        "username": name,
                        "task": task.get("title"),
                        "completed": task.get("completed")})
        db[_id] = lis

    with open('todo_all_employees.json', 'w') as _file:
        _file.write(json.dumps(db))
