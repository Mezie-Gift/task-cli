#!/usr/bin/python

import json
import os
import sys
from datetime import datetime

""" This module helps a user modify or update a task."""
def updateTask():
    """This function updates a task description from the command line."""

    taskFile = 'tasks.json'
    taskInfo = []

    # Ensure the correct number of arguments are provided.
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} {ays.argv[1]} \"<task ID>\" \"<updated description\"")
        print(f"ERROR: 3 arguments expected, {len(sys.argv) - 1} given!")
        sys.exit(1)

    taskID = sys.argv[2]
    updatedTaskDescription = sys.argv[3]

    # Ensure file exists
    if os.path.exists(taskFile):
        try:
            with open(taskFile, 'r') as data:
                taskInfo = json.load(data)
        except json.JSONDecodeError as e:
            print(f"Error Parsing JSON: {e}")
            sys.exit()
    # Search out and update a task using its id
    found = False
    for task in taskInfo:
        if task['id'] == int(taskID):
            task['description'] = updatedTaskDescription
            task['updatedAt'] = str(datetime.now())
            found = True
            description = task['description']
            print(f"The task with an ID: {taskID} has been successfully updated to '{description}'")
            break
    # If task with search id is not found 
    if not found:
        print(f"Error: no task was found with ID: {'taskIF'}")

    # Write the updated list back to the file
    try:
        with open(taskFile, 'w') as data:
            json.dump(taskInfo, data, indent=4)
    except json.JSONDecodeError as e:
        print(f"Error Parsing JSON: {e}")
        sys.exit()
