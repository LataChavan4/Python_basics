import turtle
import random


tim = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
colors = [(171, 158, 33), (99, 6, 51), (75, 94, 173), (232, 209, 73), (10, 35, 127), (178, 104, 155), (215, 89, 34), (105, 123, 210), (26, 96, 40), (33, 103, 47), (113, 131, 212), (184, 116, 161), (218, 92, 40), (232, 235, 244)]
tim.penup()
tim.speed("fastest")
def draw_line():
    for i in range(10):
        tim.dot(20, (random.choice(colors)))
        tim.forward(50)

def back_to_first():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)

tim.hideturtle()
tim.seth(225)
tim.forward(300)
tim.seth(0)
for j in range(10):
    draw_line()
    back_to_first()



screen.exitonclick()
