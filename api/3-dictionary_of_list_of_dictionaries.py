#!/usr/bin/python3
"""
place holder
"""


if __name__ == "__main__":
    import requests
    import json
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    users = users.json()
    result = {}
    for user in users:
        todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(user["id"]))
        todos = todos.json()
        result[user["id"]] = []
        for todo in todos:
            result[user["id"]].append(
                {"username": user["username"],
                    "task": todo["title"], "completed": todo["completed"]})
    with open("todo_all_employees.json", 'w') as result_file:
        json.dump(result, result_file)
