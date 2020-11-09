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

@task
def task_8_28():
    x=1
    def go():
        x=1
        while x==1: 
            if wall_is_above() == False:
                move_up(n=1)
            else:
                while x==1: 
                    if wall_is_on_the_left() == False:
                        move_left(n=1)
                    elif wall_is_on_the_left() == True:
                        x=2
                        return x           

    
    while x==1:
        if wall_is_on_the_left() == False and wall_is_above() == True:
            move_left(n=1)
          #  if wall_is_above() == False:
           #     go()
            #    x=2 
                                                    

        if wall_is_on_the_left() == True and wall_is_above() == True:   
           while x==1: 
            move_right(n=1)
            if wall_is_above() == False:
                go()            
                x=2

        if wall_is_above() == False:   
                go()            
                x=2        

                                  
if __name__ == '__main__':
    run_tasks()
