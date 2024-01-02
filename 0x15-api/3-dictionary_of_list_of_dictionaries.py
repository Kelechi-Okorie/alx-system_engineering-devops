#!/usr/bin/python3
"""For a given employee ID, returns information about
his/her TODO list progress"""

import json
import requests
import sys

if __name__ == "__main__":

    url = f"https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()

    filename = 'todo_all_employees.json'
    data = {}

    for user in users:
        tasksList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                tasksList.append({
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                })
        data[user.get('id')] = tasksList

    with open(filename, mode="w") as f:
        json.dump(data, f)
