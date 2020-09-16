#!/usr/bin/python3
"""
0x15.API module

"""
import requests
import sys


if __name__ == '__main__':
    _id = sys.argv[1]
    name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + _id).json()['name']

    data = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + _id).json()
    completed_tasks = []
    for i in data:
        if i.get("completed"):
            completed_tasks.append(i)
    print(
        'Employee {} is done with tasks({}/{}):'.format(name,
                                                        len(completed_tasks),
                                                        len(data)))
    for e in completed_tasks:
        print('\t {}'.format(e.get("title")))
