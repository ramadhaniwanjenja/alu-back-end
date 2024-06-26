#!/usr/bin/python3
"""
Python script that returns a TODO list progress for a given employee ID.

This script fetches data from the API to retrieve
and analyze the TODO list progress.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    """Step 1: Fetch employee information from the API."""
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    employee = json.loads(request_employee.text)
    employee_name = employee.get("name")
    USERNAME = employee.get("username")

    """" Step 2: Fetch the employee's TODO list from the API."""
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    tasks = {}
    employee_todos = json.loads(request_todos.text)

    USER_ID = argv[1]

    """Step 3: Analyze and process the TODO list data."""
    for dictionary in employee_todos:
        USER_ID = dictionary.get("user")
        TASK_TITLE = dictionary.get("title")
        TASK_COMPLETED_STATUS = dictionary.get("completed")
        tasks.update({TASK_TITLE: TASK_COMPLETED_STATUS})

    task_list = []
    for k, v in tasks.items():
        task_list.append({
            "task": k,
            "completed": v,
            "username": USERNAME
        })

    json_to_dump = {argv[1]: task_list}

    """ Step 4: Exporting the analyzed data to a JSON file."""
    with open('{}.json'.format(argv[1]), mode='w') as file:
        json.dump(json_to_dump, file)
