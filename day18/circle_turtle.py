from turtle import Turtle, Screen, colormode
import random

tom = Turtle()
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        tom.pencolor(random_color())
        tom.circle(150)
        tom.setheading(tom.heading() + size_of_gap)

screen = Screen()
tom.speed("fastest")
draw_spirograph(2)
screen.exitonclick()