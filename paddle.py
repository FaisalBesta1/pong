from turtle import Turtle


WIDTH = 5
LEN = 1


# Class which creates the paddles


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, starting_pos):
        super().shape("square")
        super().color("white")
        super().penup()
        super().shapesize(stretch_wid=WIDTH, stretch_len=LEN)
        super().goto(starting_pos)

    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

    # Prevents the paddles from going off the screen

    def go_up(self):
        if self.ycor() < 260:
            self.sety(self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -225:
            self.sety(self.ycor() - 20)






