from turtle import Screen
from snake import Snake
import time

screen = Screen()
# set popup screen width and height
screen.setup(width=600, height=600)

# set screen background color
screen.bgcolor("black")

# add pop up screen title
screen.title("My snake game")

# Turns turtle animation on/off and set delay for update drawings.
screen.tracer(0)

snake = Snake()

# added screen to take keypress input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move_forward()

screen.exitonclick()