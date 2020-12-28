from screen import screen, width, height
from paddles import Paddle
# paddle instance
left_paddle = Paddle(position=(-380, 0), keys=("e", "d"))
right_paddle = Paddle(position=(380, 0), keys=("Up", "Down"))
screen.update()
screen.exitonclick()
