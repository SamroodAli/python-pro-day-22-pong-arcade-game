from turtle import Turtle , onkey
from screen import screen


class Paddle(Turtle):
    def __init__(self, position, keys):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(position)
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.event_listeners(keys)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        screen.update()

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        screen.update()

    def event_listeners(self, keys):
        onkey(key=keys[0], fun=self.paddle_up)
        onkey(key=keys[1], fun=self.paddle_down)
