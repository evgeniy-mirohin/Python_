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
@task(delay=0.01)
def task_9_3():
    x=1
    y=1
    i=1
    while wall_is_on_the_right() == False:
      move_right(n=1)
      i+=1
    print (i)
    move_left(n=i-1)
    
    while True:
        print (y)
        for x in range(1,i+1):
            if x == y or x == i-y+1:       
                1==1
            else:
              fill_cell()
            if wall_is_on_the_right() == False:
                move_right(n=1)
        move_left(n=i-1)
        if x==i and y >=i:
            break
        move_down(n=1)
        y+=1

if __name__ == '__main__':
    run_tasks()
