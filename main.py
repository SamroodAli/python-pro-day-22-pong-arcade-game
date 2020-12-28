from scoreboard import ScoreBoard
from screen import screen, width, height
from paddles import Paddle
from ball import Ball
from turtle import Turtle
import time
import random
# paddle instance
left_paddle = Paddle(position=(-350, 0), keys=("w", "s"))
right_paddle = Paddle(position=(350, 0), keys=("Up", "Down"))
# scoreboard instance
scoreboard = ScoreBoard()
# ball instance
game_is_on = True
ball = Ball()
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.y_bounce()
    # Collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()
    # collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    # Detect when right paddle misses
    if ball.xcor() > 380:
        scoreboard.add_left_score()
        ball.reset_position()
    # Detect when left paddle misses
    if ball.xcor() < -380:
        scoreboard.add_right_score()
        ball.reset_position()

screen.exitonclick()
