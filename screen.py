from turtle import Screen

screen = Screen()
screen.listen()
screen.bgcolor("black")
# 1.0 takes up whole screen
screen.setup(width=800, height=600)
screen.title("Pong")
width = screen.window_width()
height = screen.window_height()
# turning animation off
screen.tracer(0)
# turning focus to event listeners on
screen.listen()
