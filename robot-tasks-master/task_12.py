#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    while True:
        if wall_is_above() == False and wall_is_beneath() == True:
            fill_cell()
        if wall_is_on_the_right() == False:
            move_right(n=1)
        else: break
            
if __name__ == '__main__':
    run_tasks()
