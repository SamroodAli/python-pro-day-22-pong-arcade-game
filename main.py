from screen import screen, width, height
from paddles import Paddle
# paddle instance
left_paddle = Paddle(position=(-380, 0))
right_paddle = Paddle(position=(380, 0))
screen.update()
screen.exitonclick()
