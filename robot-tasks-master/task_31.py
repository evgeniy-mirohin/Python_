#!/usr/bin/python3

from pyrob.api import *

# move_left(n=1)	Пройти n клеток влево (по умолчанию n = 1)
# move_right(n=1)	Пройти n клеток вправо (по умолчанию n = 1)
# move_up(n=1)	Пройти n клеток вверх (по умолчанию n = 1)
# move_down(n=1)	Пройти n клеток вниз (по умолчанию n = 1)

#   wall_is_above()	если сверху стена, возвращает True, иначе — False
#   wall_is_beneath()	если снизу стена, возвращает True, иначе — False
#   wall_is_on_the_left()	если слева стена, возвращает True, иначе — False
#   wall_is_on_the_right()	если справа стена, возвращает True, иначе — False

# fill_cell()	Закрасить текущую клетку
# cell_is_filled()	Возвращает True, если текущая клетка закрашена
@task(delay=0.05)
def task_8_30():


    x=1
    i=0
    while True:
        if wall_is_beneath() == False:
            move_down(n=1)
            i=0
            continue
        if wall_is_on_the_right() == True:
           x=1
           i+=1
        if wall_is_on_the_left() == True:
            x=0
            i+=1
        if i>1 and wall_is_on_the_left() == True and wall_is_beneath() == True:
            break            
        if x==0:
            move_right(n=1)
        if x==1:    
            move_left(n=1)

if __name__ == '__main__':
    run_tasks()
