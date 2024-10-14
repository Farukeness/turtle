import turtle
import time
import random
sc = turtle.Screen()
sc.bgcolor("light blue")
catch_turtle = turtle.Turtle()
count_turtle = turtle.Turtle()







def counter():
    count_turtle.hideturtle()
    count_turtle.up()
    height = sc.window_height()
    y = height * 0.85 /2
    count_turtle.goto(0,y)
    count_turtle.write("Score:0",align="center",font=("Arial",20,"normal"))


def random_turtle():
    catch_turtle.up()
    catch_turtle.shape("turtle")
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    catch_turtle.setposition(x,y)
    catch_turtle.stamp()
    catch_turtle.clear()
    time.sleep(1)

while True:
    turtle.tracer(0)
    counter()
    random_turtle()
    turtle.tracer(1)

turtle.mainloop()