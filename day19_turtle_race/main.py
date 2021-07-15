from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

for turtle_index in range(0, 6):
    new_t = Turtle(shape="turtle")
    new_t.penup()
    new_t.color(colors[turtle_index])
    new_t.goto(x=-230, y=-150 + turtle_index * 60)
    all_turtles.append(new_t)

if user_bet:
    is_race_on = True

while is_race_on:

    for each_turtle in all_turtles:
        if each_turtle.xcor() > 230:
            is_race_on = False
            winning_color = each_turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The winning turtle is {winning_color} turtle.")
            else:
                print(f"You've lost! The winning turtle is {winning_color} turtle.")

        random_dis = random.randint(0, 10)
        each_turtle.forward(random_dis)

screen.exitonclick()
