import turtle
import random

# Create the turtle object from Turtle class
tim = turtle.Turtle()

# set the color values are interpreted as integers between 0 and 255
turtle.colormode(255)

# Create the Screen object from Screen class
screen = turtle.Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(3)
screen.exitonclick()
