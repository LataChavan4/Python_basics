from turtle import Turtle, Screen
import random
game_on = False
screen = Screen()
colors = ["red", "blue", "green", "yellow", "pink", "orange"]
turtles =[]
screen.setup(500,400)
user_bet = screen.textinput(title="Guess", prompt="Guess the turtle which will win the race")

i = 0
for color in colors:
    tim_i = Turtle("turtle")
    tim_i.penup()
    tim_i.color(color)
    tim_i.goto((-230), (-130 + (i * 50)))
    i += 1
    turtles.append(tim_i)

if user_bet:
    game_on = True

while game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won!.{winning_color} turtle is the winner")
            else:
                print(f"sorry you lost.. {winning_color} turtle is the winner")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
