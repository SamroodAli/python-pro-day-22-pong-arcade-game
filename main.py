from screen import screen, width, height
from paddles import Paddle
from ball import Ball
import time
import random
# paddle instance
left_paddle = Paddle(position=(-380, 0), keys=("e", "d"))
right_paddle = Paddle(position=(380, 0), keys=("Up", "Down"))
# ball instance
game_is_on = True
ball = Ball()
starting_position = random.randint(0, 359)
ball.setheading(starting_position)
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce()
    # Collision with paddle
screen.exitonclick()
