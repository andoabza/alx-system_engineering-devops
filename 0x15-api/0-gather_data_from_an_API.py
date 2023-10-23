#!/usr/bin/python3
""" a script that print rest api"""
import requests
import sys

if __name__ == '__main__':
    def get_employee_todo_progress(employee_id):
        """ a function that get request api"""
        base_url = 'https://jsonplaceholder.typicode.com'
        employee_url = f'{base_url}/users/{employee_id}'
        todos_url = f'{base_url}/todos?userId={employee_id}'

        try:
            employee_response = requests.get(employee_url)
            employee_data = employee_response.json()

            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()

            total_tasks = len(todos_data)
            completed_tasks = sum(1 for todo in todos_data if todo['completed'])

            print(

                f"Employee {employee_data['name']} is done with tasks
                ({completed_tasks}/{total_tasks}): "

                )

            for todo in todos_data:
                if todo['completed']:
                    print(f"\t{todo['title']}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            sys.exit(1)

    if len(sys.argv) != 2:
        print("Usage: python script.py employee_id")
            sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
