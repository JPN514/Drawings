# python turtle test program 

import turtle 

# draws a heart on the screen using turtle
def heart():

    turtle.speed(10000)
    turtle.bgcolor("black")
    turtle.pensize(3)

    def move():
        for i in range(200):
            turtle.right(1)
            turtle.forward(1)

    turtle.color("red","red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(111.65)
    move()
    turtle.left(120)
    move()
    turtle.forward(111.65)
    turtle.end_fill()


def squares():
    # attempt to draw a square using turtle after drawing a heart:
    #turtle.left(50)
    turtle.color("white","red")
    turtle.begin_fill()
    turtle.speed(10000)
    turtle.bgcolor("black")
    turtle.pensize(3)

    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()

    # draw another square:
    turtle.left(90)
    turtle.color("white","blue")
    turtle.begin_fill()
    turtle.speed(10000)
    turtle.bgcolor("black")
    turtle.pensize(3)

    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()
squares()
squares()
squares()
squares()
turtle.done() # pauses screen after turtle finishes moving

