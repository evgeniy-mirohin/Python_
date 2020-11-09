import turtle
import math
turtle.shape('turtle')
n = 6
k=8
a = 20 
#def ugolnik(f):
for i in range(3, n, 1):
    #a= 360/i
        R = a/(2*sin(360/2*i))
        turtle.forward(R)
turtle.left((360/i)+30)
        turtle.forward(20)
        for y in range(1, i, 1):
            turtle.left((360/i))
            turtle.forward(20)
        turtle.right((30))   
        turtle.forward(20)
        
#ugolnik(n)


