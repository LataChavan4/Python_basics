from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


r_paddle = (350, 0)
l_paddle = (-350, 0)
FONT = ("Courier", 40, "normal")

screen = Screen()
screen.tracer(0)
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.listen()

screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "q")
screen.onkey(paddle_l.move_down, "a")

game_on = True
while game_on:
    time.sleep(ball.time)
    screen.update()
    ball.move_ball()
    score.score_update()

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() == -280:
        ball.bounce_y()

    ## Delecting collision with paddle_r
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        print("bounce")

    if ball.xcor() > 380:
        ball.reset_ball()
        ball.bounce_x()
        score.increase_score_l()

    if ball.xcor() < -380:
        ball.reset_ball()
        ball.bounce_x()
        score.increase_score_r()



score_l.update_scoreboard()
score_r.update_scoreboard()

screen.exitonclick()



