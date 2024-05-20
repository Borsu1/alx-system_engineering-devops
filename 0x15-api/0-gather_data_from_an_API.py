#!/usr/bin/python3
"""
This module provides a function to fetch and display an employee's TODO list progress
from the JSONPlaceholder API.
"""

import requests
import sys

def get_employee_todo_list_progress(employee_id):
    """
    Fetch and display an employee's TODO list progress from the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Fetch employee data
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = employee_response.json()

    # Fetch TODOs for the employee
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos = todos_response.json()

    # Calculate the progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo.get('completed')])
    employee_name = employee.get('name')

    # Display the progress
    print(f'Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):')

    # Display the titles of completed tasks
    for todo in todos:
        if todo.get('completed'):
            print('\t ' + todo.get('title'))

# Accept employee ID as a command-line argument
if __name__ == "__main__":
    get_employee_todo_list_progress(int(sys.argv[1]))
