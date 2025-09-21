"""
Capstone Project – Task Manager CLI
What you should know: Combine variables, data types, strings, control flow,
loops, functions, lists, dictionaries, nested data, multiple return values, error handling,
 and file handling into one cohesive program.

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

"""-------------------------------Notes------------------------------------
*use parameters when using variables from other functions
*return is used to pass variables from one function to another
*task_list should remain outside the loop so that it doesn't keep resetting
*return None, None is a placeholder indicating there is nothing to add 
and lets the list() skip invalid data without crashing
*dont need an else if the if statement has a return that ends the function early
*Use .strip() for input to make sure there isn't whitespace that causes error.
"""

#Todo 2: Mention low, medium, high besides number
#Todo 3: Sort the tasks by priority
#todo 5: only ask if a person wants to delete if there is an existing list
#Todo 6: have user be able to edit a task

# ----------------------------------------------------------------------------------------------------------------------------------------------
import os
task_list = {}

# This function will help load existing tasks.txt into the task_list dictionary if existent and if not will assign to an empty dictionary.
def load_tasks():
    tasks = {}
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    if " with a priority of " in line:
                        task, priority = line.split(" with a priority of ")
                        tasks[task] = int(priority)
    return tasks

#This function checks if both parameters(task and priority) are valid, and appends them to the dictionary(task_list).
def append_to_list():
    task,priority = ask()
    if task and priority:
        task_list[task] = priority
        print(f"Added task: {task.capitalize()} with a priority value of: {priority}.\n")
        save_tasks()

#This function takes contents of the task_list dictionary and writes them into tasks.txt.
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task, priority in task_list.items():
            file.write(f"{task.capitalize()} with a priority of {priority}\n")

#This function prints the task_list if present and lets the user know if it's empty.
def view_list():
    if not task_list:
        print("The dictionary is empty!")
    else:
        print("\nYour list(dictionary) consists of:")
        for t,p in task_list.items():
            print(f"- {t.capitalize()} with a priority of {p}.")

# This function reads the existing tasks.txt file if it exists and lets the user know if it doesn't.
def read_tasks_file():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            content = file.read().strip()
            if content:
                print(f"Your Todo list(txt file) consists of:\n {content}")
            else:
                print("Your Todo list is empty!")
    else:
        print("There is no current existing to-do list.")

def deletion():
    if os.path.exists("tasks.txt"):
        delete = input("If you would like to delete a task from your list, type 'task', if you would like to delete the entire list, type '")

# This function handles deleting the entire to-do list.
def delete_tasks_file():
    if os.path.exists("tasks.txt"):
        if task_list != {}:
            delete_list = input("Would you like to delete the current To-Do list?('y' or 'n')")
            if delete_list.lower() == "y":
                double_check = input("Are you sure you want to delete your current To-do list?('y' or 'n')")
                if double_check.lower() == "y":
                    os.remove("tasks.txt")
                    print("Success! You have deleted your to-do list!")
                elif double_check.lower() == "n":
                    pass
                else:
                    "Please type either 'y' or 'n"

#This function handles deleting a singular task.
#Todo 1: List all takss before asking which one they want to delete
#Todo 2:
def delete_task():
    if os.path.exists("tasks.txt"):
        if task_list != {}:
            delete_task = input("Would you like to delete a task on your list?('y' or 'n')")
            if delete_task.lower() == "y":
                read_tasks_file()
                #Can you combine .lower() and .capitalize()???
                select_task_for_deletion = input("Which task would you like to delete?").lower()
                del task_list[select_task_for_deletion.capitalize()]
                save_tasks()
                print(f"Success! {select_task_for_deletion} has been deleted! This is your current task list: {task_list}")
            elif delete_task.lower() == "n":
                pass

#This function asks the user if they want to delete/view/add to their to-do list.
# It also handles duplicates(case sensitive), tasks that are numerical, and priority rankings that aren't.
def ask():
    task = input("What task would you like to add to your list? To view list simply type 'list'.\n").strip()
    if task.lower() == "list":
        view_list()
        read_tasks_file()
        if view_list:
            delete_task()
            delete_tasks_file()
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

def priority():
    priority = int(input("Is this a high, medium or low priority task? 1 = High, 2 = Medium, 3 = Low)\n"))
    if priority not in [1, 2, 3]:
        print("Please enter a valid number.")

task_list = load_tasks()
while True:
    append_to_list()

