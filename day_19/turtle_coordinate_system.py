import random
from turtle import Turtle, Screen
turtles = []
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen = Screen()
screen.setup(width=500, height=400)
y = -100
is_start = False
for i in range(6):
    t = Turtle("turtle")
    t.penup()
    t.color(colors[i])
    t.goto(-230, y)
    y += 40
    turtles.append(t)

guess = screen.textinput("Question!", "Which color of turtle will win? : ")
if guess != "":
    is_start = True

while is_start:

    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 230:
            is_start = False
            winner_color = turtle.pencolor()
            if winner_color == guess:
                print(f"You win! Winner color: {winner_color}")
            else:
                print(f"You lost! Winner color: {winner_color}")

screen.exitonclick()
