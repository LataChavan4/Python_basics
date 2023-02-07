import random
from turtle import Turtle, Screen

turtle.colormode(255)
timmy = Turtle()
screen = Screen()

timmy.speed(11)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


for i in range(72):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(5)
screen.exitonclick()

