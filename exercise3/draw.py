import turtle
ram=turtle.Screen()
pen=turtle.Turtle()
pen.speed()
a=100
b=50
for i in range(2000):
    pen.forward(a)
    pen.left(90)
    pen.forward(b)
    pen.left(90)
    a=a+100
    b=b+50




turtle.done()
