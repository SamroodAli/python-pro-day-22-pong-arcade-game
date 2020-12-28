from screen import screen, width, height
from paddles import Paddle
from ball import Ball
from turtle import Turtle
import time
import random
# paddle instance
left_paddle = Paddle(position=(-350, 0), keys=("e", "d"))
right_paddle = Paddle(position=(350, 0), keys=("Up", "Down"))
# ball instance
game_is_on = True
ball = Ball()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce()
    # Collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
    # collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

screen.exitonclick()
