from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
STARTING_POSITIONS = [(350, 0), (-350, 0)]


score = Scoreboard()
r_paddle = Paddle(STARTING_POSITIONS[0])
l_paddle = Paddle(STARTING_POSITIONS[1])
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

sleep = 0.1

pong_is_on = True
while pong_is_on:
    time.sleep(sleep)
    screen.update()
    ball.first_move()
    r_paddle.go_up()
    r_paddle.go_down()
    l_paddle.go_up()
    l_paddle.go_down()

    # Stops the ball from leaving the screen

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce()

    # when ball touches paddle, speed increases

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        sleep -= 0.01

    # score update for the respective side

    if ball.xcor() > 400:
        score.left_increase()
        ball.reset_pos()
        sleep = 0.1

    elif ball.xcor() < -400:
        score.right_increase()
        ball.reset_pos()
        sleep = 0.1

screen.exitonclick()
