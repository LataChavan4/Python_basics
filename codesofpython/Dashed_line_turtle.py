from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
for i in range(10):
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)
screen.exitonclick()
