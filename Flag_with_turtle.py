#Indian Flag 
#Created by error_at_night.


from turtle import Turtle , Screen, onclick
import random

Position=[(0,200),(0,150),(0,100),(0,230)] #Position of Turtles for Orange , White, Green, Brown Color.
Color=["Orange","White","Green","brown"] #list of Colors.
FColor=["red","orange","white","pink","blue","yellow"] #List Stores Color For Flowers.
ladderPos=[(-50,-90),(-100,-120),(-200,-150)] #Store Position of Different Position.
forwardpos=[100,200,400]  #Length of each Ladder.
screen=Screen()
screen.bgcolor("black")  #Used to Change Background Color.

#The Below Loop is used to Generate Tri-Colors of Indian Flag.
for i in range(0,3):
    orange=Turtle()
    orange.speed(0)
    orange.hideturtle()
    orange.setposition(Position[i]) # Take Position from List Declared above.
    orange.color(Color[i])
    orange.pensize(50)
    orange.forward(250)

#The Stick Turtle is used to Draw The Stand of Flag.
stick=Turtle()
stick.speed(0)
stick.hideturtle()
stick.pensize(50)
stick.setposition(Position[3])
stick.setheading(270)
stick.color(Color[3])
stick.forward(300)


#The Below Loop is used to Create 3 Turtle which is further used for,
#Generating Ladder of Different Size.
for i in range(3):
    lad=Turtle()
    lad.speed(0)
    lad.penup()
    lad.hideturtle()
    lad.pensize(30)
    lad.color("brown")
    lad.setposition(ladderPos[i])
    lad.pendown()
    lad.forward(forwardpos[i])


#Used To Generate a Circle in White Strips.
Ashok=Turtle()
Ashok.speed(0)
Ashok.hideturtle()
Ashok.penup()
Ashok.pencolor("blue")
Ashok.setposition(120,125)
Ashok.pendown()
Ashok.circle(25)

#Genearte 24 Stripes of Ashoka Chakra.
#How?
#Find the Center of Circle and Draw 24 stripes for Center to edge of Circle i.e 25
#Below Loop Shows the Complete Code
for i in range(24):
    chakra=Turtle()
    chakra.hideturtle()
    chakra.speed(0)
    chakra.penup()
    chakra.setposition(120,150)
    chakra.setheading(90+(i*15))
    chakra.color("blue")
    chakra.pendown()
    chakra.forward(25)

#Not Important.
#Its is used to Generate Some Flowers , Flowers are Represented with Circle.
for i in range(50):
    flower=Turtle()
    flower.speed(0)
    flower.hideturtle()
    flower.penup()
    flower.setposition(random.randint(0,200),random.randint(-150,80))
    flower.pencolor(random.choice(FColor))
    flower.pendown()
    flower.circle(random.randint(2,4))

screen.exitonclick() #Used to exit Turtle Screen.