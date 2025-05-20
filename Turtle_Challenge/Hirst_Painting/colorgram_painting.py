import turtle
import random

# set the color values are interpreted as integers between 0 and 255
turtle.colormode(255)

# create the turtle object from Turtle class
tim = turtle.Turtle()

# create the Screen object from Screen class
screen = turtle.Screen()

color_list = [(233, 233, 232), (231, 233, 236), (234, 230, 232), (224, 232, 226), (208, 160, 81), (55, 88, 130),
              (145, 91, 40), (140, 27, 48), (221, 207, 106), (133, 177, 203)]

# when moves will not draw a line
tim.penup()

# this makes the shape invisible
tim.hideturtle()

# set object moving speed
tim.speed("fastest")

# set object moving direction
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(16, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# keeps the graphic window open until click within it
screen.exitonclick()