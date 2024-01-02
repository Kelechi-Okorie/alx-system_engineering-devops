#!/usr/bin/python3
"""For a given employee ID, returns information about
his/her TODO list progress"""

import json
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

    filename = id + '.json'
    data = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(id):
            taskList.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.get('username')
            })
    data[id] = taskList

    with open(filename, mode="w") as f:
        json.dump(data, f)
