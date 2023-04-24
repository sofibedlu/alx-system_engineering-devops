#!/usr/bin/python3
"""
Python script that, uses REST API, for a given employee ID, returns
information about his/her TODO list progress.
script accept an integer as a parameter, which is the employee ID
export data in the CSV format
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name: USER_ID.csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    api = 'https://jsonplaceholder.typicode.com'
    user_id = int(sys.argv[1])
    url_user = '{}/users/{}'.format(api, user_id)
    url_todos = '{}/todos?userId={}'.format(api, user_id)
    res_user = requests.get(url_user)
    res_todos = requests.get(url_todos)
    user_name = res_user.json().get('username')
    data = []
    row = []
    for todo in res_todos.json():
        row.append(f"{user_id}")
        row.append(f"{user_name}")
        row.append(f"{todo.get('completed')}")
        row.append(f"{todo.get('title')}")
        data.append(row)
        row = []

    file_name = "{}.csv".format(user_id)
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for row in data:
            writer.writerow(row)
