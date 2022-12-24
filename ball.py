from turtle import Turtle

# Class which creates the ball


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        super().shape("circle")
        super().color("white")
        self.y_move = 10
        self.x_move = 10

    def first_move(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_pos(self):
        self.setpos(0, 0)
        self.paddle_bounce()








