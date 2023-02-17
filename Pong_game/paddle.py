from turtle import Turtle
r_paddle = (350, 0)
l_paddle = (-350, 0)
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.resizemode('user')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed('fastest')
        self.goto(position)
## paddla movement###
    def move_up(self):
        new_y = (self.ycor()) + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = (self.ycor()) - 20
        self.goto(self.xcor(), new_y)



