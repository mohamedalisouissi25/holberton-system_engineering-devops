#!/usr/bin/python3
"""
API module

"""
import csv
import requests
import sys


if __name__ == '__main__':
    _id = sys.argv[1]
    name = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + _id).json()['username']
    data = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + _id).json()

    # csv
    with open('{}.csv'.format(_id), 'w') as csv_file:
        for i in data:
            csv_file.write("\"{}\", \"{}\", \"{}\", \"{}\"\n".format(
                                                            _id,
                                                            name,
                                                            i.get("completed"),
                                                            i.get("title")))
