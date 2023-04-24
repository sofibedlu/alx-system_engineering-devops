#!/usr/bin/python3
""" Python script that, uses REST API, for a given employee ID, returns
    information about his/her TODO list progress.
    -script accept an integer as a parameter, which is the employee ID
"""
import requests
import sys


if __name__ == "__main__":
    api = 'https://jsonplaceholder.typicode.com'
    id = int(sys.argv[1])
    url_user = '{}/users/{}'.format(api, id)
    url_todos = '{}/todos?userId={}'.format(api, id)
    res_user = requests.get(url_user)
    res_todos = requests.get(url_todos)
    user_name = res_user.json().get('name')
    total_num_task = 0
    done_task = 0
    titles = []
    for item in res_todos.json():
        if item.get('completed') is True:
            done_task += 1
            titles.append(item.get('title'))
        total_num_task += 1
    print("Employee {} is done with tasks({}/{}):".format(
                    user_name,
                    done_task,
                    total_num_task))
    for title in titles:
        print("\t {}".format(title))
