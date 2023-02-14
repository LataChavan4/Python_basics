import turtle
from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    head: Turtle

    def __init__(self):
        self.tims = []


        for position in STARTING_POSITIONS:
            self.add_segment(position)
            self.head = self.tims[0]


    def add_segment(self,position):
        tim_i = Turtle("square", 20)
        tim_i.speed("slowest")
        tim_i.color("white")
        tim_i.penup()
        tim_i.goto(position)
        self.tims.append(tim_i)

    def extend(self):
        self.add_segment(self.tims[-1].position())

    def move(self):
        for i in range((len(self.tims) - 1), 0, -1):
            x_cor = self.tims[i - 1].xcor()
            y_cor = self.tims[i - 1].ycor()
            self.tims[i].goto(x_cor, y_cor)
        self.head.forward(20)

    def up (self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down (self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right (self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left (self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

