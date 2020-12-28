from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 80, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.goto(0, 200)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"{self.left_score} : {self.right_score}", align=ALIGN, font=FONT)

    def add_left_score(self):
        self.left_score += 1
        self.update_score()

    def add_right_score(self):
        self.right_score += 1
        self.update_score()
