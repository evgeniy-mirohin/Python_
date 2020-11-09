import turtle

turtle.shape('turtle')
i = 0
x = 100
n = 12

for i in range(0, n, 1):        
    turtle.left(360/n)
    turtle.forward(x)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(x)
    turtle.left(180)
    
