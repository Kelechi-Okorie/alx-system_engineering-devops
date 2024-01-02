#!/usr/bin/python3
"""For a given employee ID, returns information about
his/her TODO list progress"""

import sys
import requests

if __name__ == "__main__":
    id = sys.argv[1]

    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)
    user = response.json()
    name = user.get('name')

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()
    totalTasks = 0
    completedTasks = 0

    for task in todos:
        if task.get('userId') == int(id):
            totalTasks = totalTasks + 1
            if task.get('completed'):
                completedTasks += 1

    print('Employee {} is done with tasks ({}/{}):'
          .format(name, completedTasks, totalTasks))

    tasks = ["\t " + task.get('title') for task in todos
             if task.get('userId') == int(id) and task.get('completed')]
    print('\n'.join(tasks))
