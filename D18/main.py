from turtle import Turtle, Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")

def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for i in range(3,20):
    draw_shape(i)

screen=Screen()
screen.exitonclick()