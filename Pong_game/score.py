from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def score_update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def increase_score_l(self):
        self.l_score += 1
        self.clear()
        self.score_update()

    def increase_score_r(self):
        self.r_score += 1
        self.clear()
        self.score_update()
