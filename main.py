import turtle 
screen = turtle.Screen()
screen.bgpic("minyons.gif")
screen.title("Deneme")
t = turtle.Turtle()
t.color("white")


def move_forward():
    t.forward(5)

def rotate_left():
    t.left(5)

def rotate_right():
    t.right(5)
def clear():
    screen.clear()
def go_home():
    t.up()
    t.home()
    t.down()
    
turtle.listen()
turtle.onkey(move_forward,"Up")
turtle.onkey(rotate_left,"Left")
turtle.onkey(rotate_right,"Right")
turtle.onkey(go_home,"h")
turtle.onkey(clear,"c")
turtle.mainloop()