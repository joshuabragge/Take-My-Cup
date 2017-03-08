
import shutil
from subprocess import call

def remove_task_and_clean():
    task = '''SchTasks /Delete /tn "takemycup" /f'''
    call(task)
    print('Task removed')
    try:
        shutil.rmtree('C:\\dEkota')
    except FileNotFoundError:
        print('Files already deleted?')
    print('Files removed!')

remove_task_and_clean()
