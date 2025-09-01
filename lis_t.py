#!/usr/bin/python

import json
import os
import sys

""" This module lists task in the task file"""
def listTask():
    """ This function lists task from the task file depending on the argument provided"""

    taskFile = 'tasks.json'
    taskInfo = []
    validStatuses = ["done", "todo", "in-progress"]

    # Ensure file exists
    if os.path.exists(taskFile):
        try:
            with open(taskFile, 'r') as data:
                taskInfo = json.load(data)
        except json.JSONDecodeError as e:
            print(f"Error Parsing JSON: {e}")
            sys.exit()

    count = 0
    found = False
    print("———————————————————————")

    if not taskInfo:
        print("The list is empty!")
    # List the whole task
    elif len(sys.argv) == 2:
        for task in taskInfo:
            print(f"{task['id']}. {task['description']}")
    elif len(sys.argv) == 3:
        status = sys.argv[2]
        if status not in validStatuses:
            print("Invalid input")
        else:

            for task in taskInfo:
                # List 'done' tasks
                if status == "done" and task['status'] == "done":
                    count += 1
                    print(f"{count}. {task['description']}")
                    found = True

                # List 'todo' tasks
                elif status == "todo" and task['status']== "todo":
                    count += 1
                    print(f"{count}. {task['description']}")
                    found = True

                # List tasks that are 'in progress'
                elif status == "in-progress" and task['status'] == "in progress":
                    count += 1
                    print(f"{count}. {task['description']}")
                    found = True

            # Check if nothing was found
            if not found:
                print(f"There are no task with status {status}")
    else:
        print("Invalid input!")
    print("———————————————————————")
