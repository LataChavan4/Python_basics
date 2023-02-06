import random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

colors = ['Purple', 'Blue', 'Green', 'Orange', 'Red','Gray', 'Brown', 'Lime']
movements = [0, 90, 180, 270]

timmy.width(7)
for i in range(200):
    timmy.color(random.choice(colors))
    timmy.seth(random.choice(movements))
    timmy.forward(20)

screen.exitonclick()
