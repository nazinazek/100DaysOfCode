from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("LightPink")

my_screen = Screen()
for steps in range(100):
    for c in ('hotpink', "red", 'plum'):
        timmy.color(c)
        timmy.forward(steps)
        timmy.right(30)
my_screen.exitonclick()