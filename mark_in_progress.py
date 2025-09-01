#!/usr/bin/python

import json
import os
import sys
from datetime import datetime


""" This module marks a task to 'in progress'"""
def markInProgress():
    """ This module uses a task id from the command line to mark a task in progress"""

    taskFile = 'tasks.json'
    taskInfo = []

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} {sys.argv[1]} \"<task ID>\"")
        print(f"ERROR: 1 argument expected, {len(sys.argv) - 1} given!")
        sys.exit()

    taskID = int(sys.argv[2])

    # Ensure file exists
    if os.path.exists(taskFile):
        try:
            with open(taskFile, 'r') as data:
                taskInfo = json.load(data)
        except json.JSONDecodeError as e:
            print(f"Error Parsing JSON: {e}")
            sys.exit()

    # Search out the task to be marked 'in progress' using its id
    found = False
    for task in taskInfo:
        if task["id"] == taskID:
            found = True
            if task["status"] != 'in progress':
                task["status"] = 'in progress'
                print(f"The status of task with ID: {taskID} has been successfully updated")
                task['updatedAt'] == str(datetime.now())
            else:
                print(f"The task with an ID: {taskID} has already been marked as 'in progress'")
            break
    if not found:
        print(f"No task was found with ID: {taskID}")
        return

    # Write the updated list back to the file
    try:
        with open(taskFile, 'w') as data:
            json.dump(taskInfo, data, indent=4)
    except json.JSONDecodeError as e:
        print(f"Error Parsing JSON: {e}")
        sys.exit()
