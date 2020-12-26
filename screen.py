from turtle import Screen

screen = Screen()
screen.listen()
screen.bgcolor("black")
# 1.0 takes up whole screen
screen.setup(width=1.0, height=1.0)
screen.title("PONG - by Samrood. Thank you for playing.")
width = screen.window_width()
height = screen.window_height()
