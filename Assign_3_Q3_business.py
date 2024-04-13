#importing everything from databse cdoe as DB
import Assign_3_Q3_database as DB


def view_history():
    '''
    :return: nothing
    idex = 1
    takes tasks from Database code
    iterates thorugh in a for loop, adding an index, and places "(DONE!)" at th end
    '''
    index = 1
    tasks = DB.view_history()
    for task in tasks:
        print(f"{index}. {task[1]} (DONE!)")
        index += 1


def view_pending():
    '''
    :return: nothing
    same as view_history, but for uncompleted tasks
    '''
    index = 1
    tasks = DB.view_pending()
    for task in tasks:
        print(f"{index}. {task[1]}")
        index += 1


def add_task():
    '''
    :return: nothing
    task is assigned to user input and is then passed onto the add_task function from database code
    loop breaks so it does not repeat
    '''
    while True:
        try:
            task = input("Description: ")
            DB.add_task(task)
            break
        except Exception as e:
            print(e)


def complete_task():
    '''
    :return: nothing
    asks the user for the task id and is then passed onto the complete_task function in database code
    '''
    while True:
        try:
            task_id = int(input("Number: "))
            DB.complete_task(task_id)
            break
        except Exception as e:
            print(e)


def delete_task():
    '''
    :return: nothing
    tasks for a task id and is then passed into the delte_task function in database table
    '''
    while True:
        try:
            task_id = int(input("Number: "))
            DB.delete_task(task_id)
            break
        except Exception as e:
            print(e)


def menu():
    print("COMMAND MENU")
    print("view     - View pending tasks")
    print("history  - view completed tasks ")
    print("add      - add a task")
    print("complete - complete a task")
    print("delete   - delete a task")
    print("exit     - exit program")


def choice():
    while True:
        try:
            choice = input("\nCommand: ").lower()
            return choice
        except Exception as e:
            print(e)
