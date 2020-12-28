from screen import screen, width, height
from paddles import Paddle
from ball import Ball
import time
# paddle instance
left_paddle = Paddle(position=(-380, 0), keys=("e", "d"))
right_paddle = Paddle(position=(380, 0), keys=("Up", "Down"))
# ball instance
game_is_on = True
ball = Ball()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

screen.exitonclick()
