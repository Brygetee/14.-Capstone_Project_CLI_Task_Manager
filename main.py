"""
Capstone Project – Task Manager CLI
What you should know: Combine variables, data types, strings, control flow, loops, functions, lists, dictionaries, nested data, multiple return values, error handling, and file handling into one cohesive program that simulates real backend logic.
Practice Prompt:
Build a Task Manager CLI where users can:
Add tasks with a title and priority (1 = High, 2 = Medium, 3 = Low).
View all tasks, grouped by priority, neatly formatted.
Mark tasks as complete by their number in the list.
Save tasks to tasks.txt and reload them on startup.
Handle invalid input (non-numbers, missing file, bad task index).
Prevent duplicate tasks by title (case-insensitive).
Bonus: Show completion percentage, allow deleting tasks, or export completed tasks to another file.
"""

"""-------------------------------Notes------------------------------------
*use parameters when using variables from other functions
*return is used to pass variables from one function to another
*task_list should remain outside the loop so that it doesn't keep resetting"""

task_list = {}
#Todo 1: Create a function asking the user the task and the priority and prevent duplicate tasks and handle invalid input


def  add_task(task, priority):
    task,priority = ask_task()
    task_list[task] = priority

def view_list():
    print(task_list)

def ask_task():
    task = input("What task would you like to add to your list? To view list simply type 'list'.\n")
    # handle "list" as input
    if task.lower() == "list":
        view_list()
        return
    # handle duplicate tasks
    elif task.strip() in task_list:
        print("Oops! That's already on your list.")
    else:
        try:
            priority = int(input("Is this a high, medium or low priority task? 1 = High, 2 = Medium, 3 = Low)\n"))
            if priority not in [1,2,3]:
                print("Please enter a valid number.")
                return
        except ValueError:
            print("Please enter a numerical value")
        return task, priority

while True:

    ask_task()
    add_task()

