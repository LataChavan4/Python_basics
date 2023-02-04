import random
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

colors = ['Purple', 'Blue', 'Green', 'Orange', 'Red','Gray', 'Brown', 'Lime']
def draw_pattern(side_length, number_of_sides):
    timmy.color(random.choice(colors))
    for i in range(number_of_sides):
        timmy.forward(side_length)
        timmy.right(360/number_of_sides)


for side in range(3, 11):
    draw_pattern(100, side)
