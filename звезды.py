import turtle
import math
import time
turtle.shape('turtle')
l = 11
a=50
def star(n):
    for i in range(1, n+1, 1):
        turtle.left(180-(180/n))
        turtle.forward(a)
    time.sleep(20)
star(l)