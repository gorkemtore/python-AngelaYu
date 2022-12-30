from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def go_forward():
    t.forward(10)


def go_backward():
    t.backward(10)


def clear():
    t.home()
    t.clear()


def counter_clock_wise():

    t.setheading(t.heading()+10)


def clock_wise():

    t.setheading(t.heading()-10)


screen.listen()
screen.onkey(key="w", fun=go_forward)
screen.onkey(key="s", fun=go_backward)
screen.onkey(key="c", fun=clear)
screen.onkey(key="a", fun=counter_clock_wise)
screen.onkey(key="d", fun=clock_wise)
screen.exitonclick()
