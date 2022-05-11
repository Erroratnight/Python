from turtle import Turtle
import random

COLOR=["red","blue","white","grey","pink","brown","violet","green","sky blue","light green"]

class Turtle_class(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        #Basic Stuff to initilize the Player and Set Position 
        self.color(random.choice(COLOR))
        self.penup()
        self.hideturtle()
        self.setposition(-100,-300)
        self.setheading(90)
        self.showturtle()

    #Move Forward Sequence
    def move(self):
        self.forward(20)

    
    #Reset Sequence when Player has Reached to final line  
    def reset(self):
        self.color(random.choice(COLOR))
        self.hideturtle()
        self.setposition(-100,-300)
        self.setheading(90)
        self.showturtle()


#Just Fancy Design to Show User Finish Line
class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.hideturtle()
        self.setposition(300,300)
        self.setheading(180)
        self.pendown()
        self.forward(600)