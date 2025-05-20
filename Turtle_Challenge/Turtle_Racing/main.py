from turtle import Turtle, Screen
import random

# create object from Screen class
screen = Screen()

# set screen size in pixels
screen.setup(width=500, height=400)

# create popup window for user input at beginning
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis_pos = [-80, -40, 0, 40, 80]
turtles_list = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_axis_pos[turtle_index])
    turtles_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 222:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've WON! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
