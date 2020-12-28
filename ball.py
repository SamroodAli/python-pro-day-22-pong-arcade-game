from turtle import Turtle
from random import choice
STARTING_DIRECTIONS = [10, -10]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        # Choice is from random module
        self.x_move = choice(STARTING_DIRECTIONS)
        self.y_move = choice(STARTING_DIRECTIONS)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1