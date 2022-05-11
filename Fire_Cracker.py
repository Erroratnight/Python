from turtle import Turtle , Screen, color, position
import random , time

A=30

#Set up for the screen
screen=Screen()
screen.setup(700,700)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Fire Cracker")

for i in range(A):

    #In each loop we are assigning different parameter.
    length=random.randint(20,100)
    positionx=random.randint(-280,280)
    positiony=random.randint(-280,280)
    inc_angle=random.randint(2,6)
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)

    turtle=Turtle()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.color(r,g,b)
    turtle.setposition(positionx,positiony)
    turtle.pendown()
    screen.tracer(0)
    time.sleep(0.2)
    screen.update()

    angle=0
    while angle <=360:
        turtle.forward(length)
        turtle.penup()
        turtle.setposition(positionx,positiony)
        turtle.pendown()
        turtle.setheading(angle+inc_angle)
        angle=angle+inc_angle
screen.exitonclick()

#In firecracker we have just used forward method and again back to original position
#Repeat as many times you want.