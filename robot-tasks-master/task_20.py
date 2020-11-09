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
#

@task(delay=0.05)
def task_4_3():
    x=1
    def go(): 
       # while cell_is_filled() == True:
            
            for i in range(1, 13, 1):
                print (i)
                
                if i%2 == 1:
                    for y in range(1, 27, 1):
                        fill_cell()
                        move_right(n=1)
                    fill_cell()    
                    move_down(n=1)    
                if i%2 == 0:
                    for y in range(1, 27, 1):
                        fill_cell()
                        move_left(n=1)
                    fill_cell()
                    move_down(n=1)

    move_right(n=1)
    go()




if __name__ == '__main__':
    run_tasks()
