from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
game_on = True
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    snake.move()
    time.sleep(.1)

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.food_refresh()
        score.increase_score()
        score.update_scoreboard()
        snake.extend()

  ## Detecting collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_score()
        snake.reset()

 ## Detecting collision with tale
    for item in snake.tims[1:]:
        if snake.head.distance(item) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()
