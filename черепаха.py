import turtle

turtle.shape('turtle')
#for i in range(10):
i = 0
x = 10
x1 = 30
while i < 50:
    for i1 in range(4):
        turtle.forward(x1)
        turtle.left(90)
    turtle.penup()
    #turtle.right(90)
    turtle.forward(-15)
    turtle.right(90)
    turtle.forward(15)
    turtle.down()
    turtle.left(90)
    #turtle.forward(50)
    #turtle.right(90)
    #turtle.forward(50)
    x1+=30
    i += 1
