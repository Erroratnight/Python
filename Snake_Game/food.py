from turtle import Turtle, shape 
import random

SHAPE=["turtle", "circle"]
COLOR=["white","blue","grey","pink","brown","violet","purple","indigo"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(1,1)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        A=random.randint(1,10)
        if A==1:
            shape=SHAPE[0]
        else:
            shape=SHAPE[1]
        self.color(random.choice(COLOR))
        self.shape(shape)
        self.goto(random.randint(-250,250),random.randint(-250,250))   