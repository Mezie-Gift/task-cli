#!/usr/bin/python

import json
import os
import sys
from datetime import datetime

""" This module marks a task as done"""
def markDone():
    """This function marks a task as 'done' from the CL using the task id"""

    taskFile = 'tasks.json'
    taskInfo = []

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} {sys.argv[1]}\"<task ID>\"")
        print(f"ERROR: 2 arguments expected, {len(sys.argv) - 1} given!")
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

    # Search out the task to be marked 'done' using its id
    found = False
    for task in taskInfo:
        if task["id"] == taskID:
            found = True
            # Check if task has already been marked done
            if task['status'] != 'done':
                task['status'] = 'done'
                task['updatedAt'] = str(datetime.now())
                print(f"The task with an ID: {taskID} has been marked done!")
            else:
                print(f"The task with the ID: {taskID} is already marked as done!")
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
