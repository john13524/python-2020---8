import turtle
c = 90
b = turtle.Turtle()
a = turtle.Turtle()
b.color('red')
b.shape('turtle')
a.color('green')
a.shape('turtle')
a.pensize(11)
b.pensize(11)
for i in range(5):
    for i in range(12):
        b.right(c)
        b.forward(100)
        a.left(c)
        a.forward(100)
        b.stamp()
        a.stamp()
    for i in range(12):
        b.left(c)
        b.forward(100)
        a.right(c)
        a.forward(100)
turtle.done()
