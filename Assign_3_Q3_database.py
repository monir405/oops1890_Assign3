import sqlite3

conn = sqlite3.connect('task_list_db.sqlite')


def add_task(task):
    '''
    :param task: task is input by the user in add_task from Q3_business
    :return: nothinf
    first it selects the highest taskID number from the database and assigns to a variablr.
     variable is increased by 1 to give the task ID
     task id and the task number is isnerted into the table along with 0 (to incidae an uncompleted task)
    '''
    while True:
        try:
            conn = sqlite3.connect('task_list_db.sqlite')
            c = conn.cursor()
            c.execute("""SELECT MAX(taskID) FROM Task;""")
            max_id = c.fetchone()[0]
            max_id +=1
            c.execute(f"""INSERT INTO Task (taskID, description, completed) VALUES ({max_id}, '{task}', 0);""")
            conn.commit()
            conn.close()
            break
        except Exception as e:
            print(e)


def view_history():
    '''
    :return: tasks to the business code
    selects everything from the table that is completed (completed is 1) and returns it
    '''
    while True:
        try:
            conn = sqlite3.connect('task_list_db.sqlite')
            c = conn.cursor()
            c.execute("SELECT * FROM Task WHERE completed=1;")
            tasks = c.fetchall()
            return tasks
        except Exception as e:
            print(e)


def view_pending():
    '''
    :return: retusn task to business code
    same as view_history, but where completed is 0
    '''
    while True:
        try:
            conn = sqlite3.connect('task_list_db.sqlite')
            c = conn.cursor()
            c.execute("SELECT * FROM Task WHERE completed=0;")
            tasks = c.fetchall()
            return tasks
        except Exception as e:
            print(e)


def complete_task(task_num):
    '''
    :param task_num: input by the user in complete_task from business code
    updates the complted column to 1 where the task id is equal to that of the user input
    :return:
    '''
    while True:
        try:
            conn = sqlite3.connect('task_list_db.sqlite')
            c = conn.cursor()
            c.execute(f"UPDATE Task SET completed=1 WHERE taskID = {task_num};")
            conn.commit()
            conn.close()
            break
        except Exception as e:
            print(e)


def delete_task(task_num):
    '''
    :param task_num: input by the user in delete_task from business code
    same as complete taks, but removes it instead
    :return:
    '''
    while True:
        try:
            conn = sqlite3.connect('task_list_db.sqlite')
            c = conn.cursor()
            c.execute(f"DELETE FROM Task WHERE taskID = {task_num};")
            conn.commit()
            conn.close()
            break
        except Exception as e:
            print(e)
