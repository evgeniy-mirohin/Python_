#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while wall_is_beneath() == False:
        move_down(n=1)
    while wall_is_beneath() == True:
        move_right(n=1)
    move_down(n=1) 
    move_left(n=1)
    while wall_is_above() == True and wall_is_on_the_left() == False:
        move_left(n=1)      


if __name__ == '__main__':
    run_tasks()
