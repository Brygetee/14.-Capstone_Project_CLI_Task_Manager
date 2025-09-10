"""
Capstone Project – Task Manager CLI
What you should know: Combine variables, data types, strings, control flow, loops, functions, lists, dictionaries, nested data, multiple return values, error handling, and file handling into one cohesive program that simulates real backend logic.

Practice Prompt:
Build a Task Manager CLI where users can:
*Add tasks with a title and priority (1 = High, 2 = Medium, 3 = Low).✅
*View all tasks, grouped by priority, neatly formatted.
*Mark tasks as complete by their number in the list.
*Save tasks to tasks.txt and reload them on startup.
*Handle invalid input (non-numbers, missing file, bad task index).
*Prevent duplicate tasks by title (case-insensitive).✅
*Bonus: Show completion percentage, allow deleting tasks, or export completed tasks to another file.
"""
from importlib.resources import contents

"""-------------------------------Notes------------------------------------
*use parameters when using variables from other functions
*return is used to pass variables from one function to another
*task_list should remain outside the loop so that it doesn't keep resetting
*return None, None is a placeholder indicating there is nothing to add 
and lets the list() skip invalid data without crashing
*dont need an else if the if statement has a return that ends the function early
*Use .strip() for input to make sure there isn't whitespace that causes error.
"""
#Todo 1: Let user be able to delete task from list
#Todo 2: Mention low, medium, high besides number


import os
task_list = {}

#This function checks if both parameters(task and priority) are valid, and appends them to the dictionary(task_list).
def append_to_list():
    task,priority = ask()
    if task and priority:
        task_list[task] = priority
        #should this be a return value?
        print(f"Added task: {task.capitalize()} with a priority value of: {priority}.\n")
        #Add new value to txt file/create new txt file if non-existent.
        with open("tasks.txt","a") as file:
            file.write(f"\n{task.capitalize()} with a priority value of: {priority}.")

#This function prints the task_list if present and if empty, tells the user and asks them if they'd like to add anything.
def view_list():
    if not task_list:
        read_tasks_file()
    #     print("Looks like your list is empty.")
    else:
        for t,p in task_list.items():
            print(f"\nYour list consists of: {t.capitalize()} with a priority of {p}\n.")

def read_tasks_file():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            content = file.read().strip()
            if content:
                print(f"Your Todo list consists of:\n {content}")
            else:
                print("Your Todo list is empty!")
    else:
        print("There is no current existing To-do list.")


#This function asks the user if they want to view/add to their to-do list. It also handles duplicates(case sensitive), tasks that are numerical, and priority rankings that aren't.
def ask():
    task = input("What task would you like to add to your list? To view list simply type 'list'.\n").strip()
    if task.lower() == "list":
        # view_list()
        read_tasks_file()
        return None, None
    try:
        float(task)
        print("Tasks must consist of words, not just numbers.")
        return None, None
    except ValueError:
        pass

    if task.lower() in (t.lower() for t in task_list):
        print("Oops! That's already on your list.")
        return None, None

    try:
        priority = int(input("Is this a high, medium or low priority task? 1 = High, 2 = Medium, 3 = Low)\n"))
        if priority not in [1,2,3]:
            print("Please enter a valid number.")
            return None, None

    except ValueError:
        print("Please enter a numerical value")
        return None, None
    return task, priority

while True:
    append_to_list()

