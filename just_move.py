import turtle


sc = turtle.Screen()
sc.bgcolor("white")
t = turtle.Turtle()
t.color('black')
def up():
    t.setheading(90)
    t.forward(10)
def down():
    t.setheading(270)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

turtle.listen()
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")

turtle.mainloop()






