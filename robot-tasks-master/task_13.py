#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while True:
        if wall_is_above() == False:
            move_up(n=1)
            fill_cell()
            move_down(n=1)
        if wall_is_beneath() == False:
            move_down(n=1)
            fill_cell() 
            move_up(n=1)  
        if wall_is_on_the_right() == False:
            move_right(n=1)
        else: break


if __name__ == '__main__':
    run_tasks()
