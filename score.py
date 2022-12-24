from turtle import Turtle
FONT = ("Courier", 40, "normal")
ALIGNMENT = "center"

# Class which creates the scoreboard


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        super().penup()
        super().hideturtle()
        super().goto(0, 240)
        super().color("white")
        super().speed(0)
        self.score_file()

    def score_file(self):
        super().write(f"{self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT)

    def right_increase(self):
        super().clear()
        self.r_score += 1
        self.score_file()

    def left_increase(self):
        super().clear()
        self.l_score += 1
        self.score_file()
