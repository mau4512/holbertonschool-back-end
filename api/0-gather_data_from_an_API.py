#!/usr/bin/python3
"""
Uses REST API to return jsonplaceholder employee productivity info
Called with ./0 (employee ID number)
First line: (employee name) is done with tasks(completed/total):
Following lines: titles of completed tasks
"""

import requests
import sys


def get_employee_tasks(empID):
    """ Prints info about productivity of given employee ID """

    name = ''
    task_list = []
    completed = 0

    # Recieves API response in form of complicated dict
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(empID))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(empID))

    # Use json method to break api response into useful info (at key name)
    userJSON = user.json()
    name = userJSON.get('name')

    todoJSON = todo.json()

    # Gathers list of completed tasks and count
    for task in todoJSON:
        if task.get('completed') is True:
            completed += 1
            task_list.append(task.get('title'))

    # Prints summary of given employee
    print("Employee {} is done with tasks({}/{}):".format(
        name, completed, len(todoJSON)))
    # Prints completed tasks
    for task in task_list:
        print("\t {}".format(task))

# Only imports when called, but also passes first argument
if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
