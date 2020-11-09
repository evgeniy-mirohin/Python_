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
#mov(r, v)	Поместить значение v в регистр r
@task(delay=0.02)
def task_8_18():
    v=0
    i=0
    r=0
    while i==0:
        
        if wall_is_beneath() == True  and wall_is_above()== True: 
            fill_cell()
            move_right(n=1)
            continue
        if wall_is_above() == False and wall_is_beneath() == True :
            while wall_is_above() == False:
                move_up(n=1)
                if cell_is_filled():
                    v+=1 
                        
                    print (v)  
                if not cell_is_filled():            
                    fill_cell()
             
            while wall_is_beneath() == False: 
                fill_cell()
                move_down(n=1)
            move_right(n=1)
        if  wall_is_on_the_right() == True:
            print (v)
            i=1
    mov("ax",v)        
    


if __name__ == '__main__':
    run_tasks()
