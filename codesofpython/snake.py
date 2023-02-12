
from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.tims = []


        for i in range(0, 3):
            tim_i = Turtle("square", 20)
            tim_i.speed("slowest")
            tim_i.color("white")
            tim_i.penup()
            tim_i.goto((0 - i * 20), 0)
            self.tims.append(tim_i)


    def move (self):
        for i in range((len(self.tims) - 1), 0, -1):
            x_cor = self.tims[i - 1].xcor()
            y_cor = self.tims[i - 1].ycor()
            self.tims[i].goto(x_cor, y_cor)
        self.tims[0].forward(20)

    def up (self):
        if self.tims[0].heading() != DOWN:
            self.tims[0].seth(UP)

    def down (self):
        if self.tims[0].heading() != UP:
            self.tims[0].seth(DOWN)

    def right (self):
        if self.tims[0].heading() != LEFT:
            self.tims[0].seth(RIGHT)

    def left (self):
        if self.tims[0].heading() != RIGHT:
            self.tims[0].seth(LEFT)
