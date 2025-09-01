#!/usr/bin/python3

import os
import sys
import json
from datetime import datetime


"""This module defines and adds a task to the Task list"""
def addTask():
    """Adds a new task from a command-line argument to tasks.json."""

    taskFile = 'tasks.json'

    # Ensure that one positional argument is provided
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} {sys.argv[1]} \"<task description>\"")
        print(f"ERROR: 2 arguments expected, {len(sys.argv) - 1} given!")
        sys.exit(1)


    # Ensure file exists and assign 
    if not os.path.exists(taskFile):
        taskID = 1
        taskInfo = []
        with open(taskFile, 'w') as data:
            json.dump(taskInfo, data, indent=4)
   # Ensure file exists and is not empty then assign task id based on the serial number of tasks
    elif os.path.exists(taskFile) and os.path.getsize(taskFile) > 0:
        try:
            with open(taskFile, 'r') as data:
               taskInfo =  json.load(data)
            taskID = len(taskInfo) + 1
        except json.JSONDecodeError as e:
            print(f"Error Parsing JSON: {e}")
            sys.exit()
    # If file exists but is empty
    else:
        taskInfo = []
        taskID = 1
    # Confirm whether a task with description same as user's input exists
    for task in taskInfo:
        if task['description'] == sys.argv[2]:
            print(f"A task with the description '{sys.argv[2]}' is already in the list.")
            response = input(f"Do you want to continue to add '{sys.argv[2]}'? Enter Y or N: ")
            if response.upper() == 'Y':
                taskDescription = sys.argv[2]
            elif response.upper() == 'N':
                sys.exit()
            else:
                print("Invalid input. please enter Y or N.")

    taskDescription = sys.argv[2]

    # Task Properties
    taskDict = {
            "id" : taskID,
            "description" : taskDescription,
            "status" : 'todo',
            "createdAt": str(datetime.now()),
            "updatedAt" : None
            }
    taskInfo.append(taskDict)

    # Write task into the file (tasks.json)
    try:
        with open(taskFile, 'w') as data:
            json.dump(taskInfo, data, indent=4)
    except json.JSONDecodeError as e:
        print(f"Error Parsing JSON: {e}")
        sys.exit()

    print(f"'{sys.argv[2]}' successfully added to the task list!")
