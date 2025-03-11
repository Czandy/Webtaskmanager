Fi = "tasks.txt"

def get_tasks(filepath = Fi):
    with open(filepath, 'r') as file_local:
        taskslocal = file_local.readlines()
    return taskslocal


def write_tasks(task_arg, filepath= Fi):
    with open(filepath, 'w') as file:
        file.writelines(task_arg)


def get_completetasks(filepath = 'donetasks.txt'):
    with open(filepath, 'r') as complete:
        completetasks = complete.readlines()
    return completetasks

def write_completetasks(task_arg, filepath='donetasks.txt'):
    with open(filepath, 'w') as file:
        file.writelines(task_arg)

