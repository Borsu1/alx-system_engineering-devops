#!/usr/bin/python3
"""
This module provides a function to fetch TODO lists from all employees from the
JSONPlaceholder API and export the data in JSON format.
"""

import json
import requests


def get_all_employees_todo_list():
    """
    Fetch TODO lists from all employees from the JSONPlaceholder API and export
    the data in JSON format.

    Returns:
        None
    """
    # Fetch all users
    users_response = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    users = users_response.json()

    # Prepare data for JSON
    data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        # Fetch TODOs for the user
        todos_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
        todos = todos_response.json()

        data[user_id] = [
            {
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            }
            for todo in todos
        ]

    # Write data to JSON
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file, indent=4)


# Run the function
if __name__ == "__main__":
    get_all_employees_todo_list()
