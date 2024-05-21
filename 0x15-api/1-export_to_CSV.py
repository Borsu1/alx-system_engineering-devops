#!/usr/bin/python3
"""
This module provides a function to fetch an employee's TODO list from the
JSONPlaceholder API and export the data in CSV format.
"""

import csv
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    """
    Fetch an employee's TODO list from the JSONPlaceholder API and export the
    data in CSV format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Fetch employee data
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(url)
    employee = employee_response.json()

    # Fetch TODOs for the employee
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(url)
    todos = todos_response.json()

    # Prepare data for CSV
    data = []
    for todo in todos:
        data.append([
            employee_id,
            employee.get('username'),
            todo.get('completed'),
            todo.get('title')
        ])

    # Write data to CSV
    with open(f'{employee_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)


# Accept employee ID as a command-line argument
if __name__ == "__main__":
    get_employee_todo_list_progress(int(sys.argv[1]))
