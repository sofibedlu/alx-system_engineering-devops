#!/usr/bin/python3
""" Python script that, uses REST API, for a given employee ID, returns
    information about his/her TODO list progress.
    -script accept an integer as a parameter, which is the employee ID
    -export data in the JSON formati
    -Records all tasks from all employees
    -Format: { "USER_ID": [{"task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    -file name: USER_ID.json
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    api = 'https://jsonplaceholder.typicode.com'
    url_user = '{}/users/{}'.format(api, user_id)
    url_todos = '{}/todos?userId={}'.format(api, user_id)
    res_todos = requests.get(url_todos).json()
    user_name = requests.get(url_user).json().get('username')
    obj = {}
    dicts = {}
    value = []

    for task in res_todos:
        obj["task"] = task.get('title')
        obj["completed"] = task.get('completed')
        obj["username"] = user_name
        value.append(obj)
        obj = {}
    dicts[f"{user_id}"] = value

    file_name = '{}.json'.format(user_id)
    with open(file_name, 'w') as fil:
        json_str = json.dump(dicts, fil)
