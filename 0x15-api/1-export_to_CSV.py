#!/usr/bin/python3
""" a script that save to csv file"""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    f = f"{employee_id}.csv"

    with open(f, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in todos_data:
            writer.writerow([
                employee_id, employee_data['username'],
                todo['completed'], todo['title']])
