#!/usr/bin/python3
"""
This module provides a function to fetch an employee's TODO list from the
JSONPlaceholder API and export the data in JSON format.
"""

import json
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    """
    Fetch an employee's TODO list from the JSONPlaceholder API and export the
    data in JSON format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Fetch employee data
    employee_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )
    employee = employee_response.json()

    # Fetch TODOs for the employee
    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )
    todos = todos_response.json()

    # Prepare data for JSON
    data = {employee_id: []}
    for todo in todos:
        data[employee_id].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": employee.get('username')
        })

    # Write data to JSON
    with open(f'{employee_id}.json', 'w') as file:
        json.dump(data, file, indent=4)


# Accept employee ID as a command-line argument
if __name__ == "__main__":
    get_employee_todo_list_progress(int(sys.argv[1]))
