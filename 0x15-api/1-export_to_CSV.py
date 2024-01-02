#!/usr/bin/python3
"""For a given employee ID, returns information about
his/her TODO list progress"""

import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]

    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)
    user = response.json()
    name = user.get('username')

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()

    filename = id + '.csv'
    with open(filename, mode="w") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')

        for task in todos:
            if task.get('userId') == int(id):
                writer.writerow([id, name, str(task.get('completed')),
                                 task.get('title')])
