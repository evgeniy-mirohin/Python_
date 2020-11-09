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
@task(delay=0.1)
def task_7_5():
    x=0
    #i=0
    move_right(n=1)
    fill_cell()
    while wall_is_on_the_right()== False:
        for i in range(0, x ,1):
            if wall_is_on_the_right()== False:
                move_right(n=1)
                print (x)
                print (i)
            if  i == x-1:
                fill_cell()
            if wall_is_on_the_right()== True:
                break


        x+=1 
    #break       
   # while wall_is_on_the_right()== False:
   #  move_right(n=1)





if __name__ == '__main__':
    run_tasks()
