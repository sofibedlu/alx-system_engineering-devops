#!/usr/bin/python3
""" Python script that, uses REST API, for a given employee ID, returns
    information about his/her TODO list progress.
    -script accept an integer as a parameter, which is the employee ID
    -export data in the JSON format
    -Records all tasks from all employees
    -Format: { "USER_ID": [ {"username": "USERNAME", "task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
    "USER_ID":[ {"username": "USERNAME", "task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ... ]}

    -File name: todo_all_employees.json
"""
import json
import requests


if __name__ == "__main__":
    api = 'https://jsonplaceholder.typicode.com'
    url_todos = '{}/todos'.format(api)
    res_todos = requests.get(url_todos)
    obj = {}
    dicts = {}
    value = []
    user_ids = []

    for todo in res_todos.json():
        if todo.get('userId') not in user_ids:
            user_ids.append(todo.get('userId'))

    for user_id in user_ids:
        url_user = '{}/users/{}'.format(api, user_id)
        user_name = requests.get(url_user).json().get('username')
        url_todos = '{}/todos?userId={}'.format(api, user_id)
        res_todos = requests.get(url_todos).json()
        for task in res_todos:
            obj["username"] = user_name
            obj["task"] = task.get('title')
            obj["completed"] = task.get('completed')
            value.append(obj)
            obj = {}
        dicts["{}".format(user_id)] = value
        value = []

    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as fil:
        json_str = json.dump(dicts, fil)
