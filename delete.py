#!/usr/bin/python

import json
import os
import sys

""" This module deletes a task from the task file"""
def deleteTask():
    """ This function deletes a task from the command line using its id"""

    taskFile = 'tasks.json'
    taskInfo = []
    
    # Ensure the correct number of argument is provided
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} {sys.argv[1]} \"<task ID>\"")
        print(f"ERROR: 2 arguments expected, {len(sys.argv) - 1} given!")
        sys.exit(1)

    taskID = sys.argv[2]

    # Ensure file exists
    if os.path.exists(taskFile):
        try:
            with open(taskFile, 'r') as data:
                taskInfo = json.load(data)
        except json.JSONDecodeError as e:
            print(f"Error Parsing JSON: {e}")
            sys.exit()

    # Search out the task to be deleted using its id
    found = False
    for index, task in enumerate(taskInfo):
        if task.get("id") == int(taskID):
            taskInfo.pop(index)
            found = True
            print(f"Task with the description '{task['description']}' successfully deleted!")
            break
    if not found:
        print(f"No task was found with ID: {taskID}")
        return

    # Reasign id to the tasks in the file
    count = 0
    for task in taskInfo:
        count += 1
        task["id"] = count


    # Write the updated list back to the file
    try:
        with open(taskFile, 'w') as data:
            json.dump(taskInfo, data, indent=4)
    except json.JSONDecodeError as e:
        print(f"Error Parsing JSON: {e}")
        sys.exit()
