#!/usr/bin/python3
import requests
import sys

employ_id = int(sys.argv[1])
USER_URL = f"https://jsonplaceholder.typicode.com/users/{employ_id}"
TASKS_URL = f"https://jsonplaceholder.typicode.com/todos/?userId={employ_id}"

emp_name = requests.get(USER_URL).json()['name']
todos = requests.get(TASKS_URL).json()
completed = 0
number_of_tasks = len(todos)

for todo in todos:
    if todo['completed']:
        completed += 1
    


if __name__ == "__main__":
    print(f"Employee {emp_name} is done with tasks ({completed}/{number_of_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(" ",todo["title"])
