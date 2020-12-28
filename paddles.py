from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
