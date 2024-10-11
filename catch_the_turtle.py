import turtle
import time
import random
sc = turtle.Screen()
sc.bgcolor("light blue")

catch_turtle = turtle.Turtle()




def random_turtle():
    
    catch_turtle.shape("turtle")
    catch_turtle.up()
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    catch_turtle.goto(x,y)
    catch_turtle.stamp()
    time.sleep(0.2)
    catch_turtle.clear()


random_turtle()

turtle.mainloop()