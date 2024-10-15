import turtle
import time
import random
sc = turtle.Screen()
sc.bgcolor("light blue")
count_turtle = turtle.Turtle()
count_turtle.hideturtle()
count_turtle.up()
catch_turtle = turtle.Turtle()
catch_turtle.shape("turtle")
timer_turtle = turtle.Turtle()
timer_turtle.up()
timer_turtle.hideturtle()
score = 0
game =True

def counter():
    global score
    height = sc.window_height()
    y = height * 0.85 /2
    count_turtle.goto(0,y)
    count_turtle.write("Score:0",align="center",font=("Arial",20,"normal"))
def timer(time):
    global game
    timer_turtle.clear()
    height = sc.window_height()
    y = height * 0.75 /2
    timer_turtle.goto(0,y)
    if time > 0:
        timer_turtle.write(f"Time:{time}",align="center",font=("Arial",20,"normal"))
        sc.ontimer(lambda:timer(time-1),1000)
    else:
        timer_turtle.write("Game Over",align="center",font=("Arial",20,"normal"))
        catch_turtle.hideturtle()
        game = False


def random_turtle():
    def handle_click(x,y):
        global score
        score += 1
        count_turtle.clear()
        count_turtle.write(f"Score:{score}",align="center",font=("Arial",20,"normal"))
        
    if game:
        catch_turtle.onclick(handle_click)
        catch_turtle.up()
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        catch_turtle.setposition(x,y)
        catch_turtle.stamp()
        catch_turtle.clear()
        sc.ontimer(random_turtle,500)
      
    
    
    
    
    
    


turtle.tracer(0)
counter()
timer(5)
random_turtle()
turtle.tracer(1)    

turtle.mainloop()