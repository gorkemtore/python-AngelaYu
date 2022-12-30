from turtle import Turtle, Screen, colormode
import random

tim = Turtle()

# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
#
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#
# polly = 4
# angle = 360 / polly
# for i in range(8):
#     for _ in range(polly):
#         tim.forward(100)
#         tim.left(angle)
#     polly += 1
#     angle = 360/polly

# #colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# #"SeaGreen"]
# colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#

# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")
# for i in range(200):
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(directions))
#
#


colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
tim.pensize(2)


def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()

