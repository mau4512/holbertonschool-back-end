#!/usr/bin/python3
"""
Uses REST API to return jsonplaceholder employee productivity info
Writes gathered info to .json file
Called with ./2 (employee ID number)
"""

import json
import requests
import sys


def export_to_json(empID):
    """ Prints info about all tasks for given employee ID to json file """

    name = ''
    userDict = {}

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(empID))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(empID))

    userJSON = user.json()
    name = userJSON.get('username')

    todoJSON = todo.json()

    # userDict at key empID is list, everything else is value
    userDict[empID] = []

    # Format is: {empID: [{task key: task value}, {task key: task value}]}
    for task in todoJSON:
        # Each taskDict should have format:
        #   "task": "value", "username": "value", "completed": true/false
        taskDict = {}
        taskDict["task"] = task.get('title')
        taskDict["username"] = name
        taskDict["completed"] = task.get('completed')

        # When each taskDict is built properly, add to final dict at empID key
        userDict[empID].append(taskDict)

    # Write to empID.json file
    with open("{}.json".format(empID), 'w') as jsonFile:
        json.dump(userDict, jsonFile)

# Only imports when called, but also passes first argument
if __name__ == "__main__":
    export_to_json(sys.argv[1])
