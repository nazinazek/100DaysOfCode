from turtle import Turtle, Screen, colormode
import random

tom = Turtle()
colormode(255)

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tom.forward(100)
        tom.setheading(angle)

def random_walk(range_number):
    tom.speed(0)
    for _ in range (range_number):
        tom.pencolor(random_color())
        tom.forward(30)
        tom.right(random.choice(directions))

tom.pensize(10)
random_walk(200)
