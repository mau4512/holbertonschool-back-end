#!/usr/bin/python3
"""
Uses REST API to return jsonplaceholder employee productivity info
Writes gathered info to .json file
"""

import json
import requests

if __name__ == "__main__":
    """ Prints info about all employees to json file """

    allDict = {}
    userDict = {}

    users = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    userJSON = users.json()
    todoJSON = todos.json()

    # Sets up multiple lists for info about each user
    for user in userJSON:
        userDict[user['id']] = user['username']

    # Format is: {empID: [{task key: task value}, {task key: task value}]}
    for task in todoJSON:
        # Creates new list for each user if valid userID
        if allDict.get(task['userId'], False) is False:
            allDict[task['userId']] = []
        # Each user list should have format:
        #   empID: name, True/False if completed, task title
        taskDict = {}
        # Dict format is userId as key, info about tasks as value (in order)
        taskDict["username"] = userDict[task['userId']]
        taskDict["task"] = task['title']
        taskDict["completed"] = task['completed']
        # When each taskDict is built properly, add to final dict
        allDict[task['userId']].append(taskDict)

    # Writes to json file
    with open('todo_all_employees.json', 'w') as jsonFile:
        json.dump(allDict, jsonFile)
