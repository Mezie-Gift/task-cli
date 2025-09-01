#!/usrbin/python3

from add import addTask
from update import updateTask
from delete import deleteTask
from mark_done import markDone
from mark_in_progress import markInProgress
from lis_t import listTask

import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        sys.exit()

    command = sys.argv[1]

    if command == "add":
        addTask()
    elif command == "update":
        updateTask()
    elif command == "delete":
        deleteTask()
    elif command == "mark-done":
        markDone()
    elif command == "mark-in-progress":
        markInProgress()
    elif command == "list":
        listTask()
    else:
        print("Error: Invalid command")
        sys.exit()
