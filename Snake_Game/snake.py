import random
from turtle import Turtle
POSITION=[(0,0),(-20,0),(-40,0)]
MOVE=20
COLOR=["white","blue","grey","pink","brown","violet","purple","indigo"]
UP=90
DOWN=270
RIGHT=0
LEFT=180

     
class Snake:
    def __init__(self):
        self.Body=[]
        self.create_snake()
        self.head=self.Body[0]
        self.head.color("red")
        self.head.shape("arrow")

    def create_snake(self):
        for i in POSITION:
            self.add_body(i)
            

    def snake_move(self):
            for body in range(len(self.Body)-1,0,-1):
                self.Body[body].goto(self.Body[body-1].position())

            self.head.forward(MOVE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_body(self.Body[-1].position())


    def add_body(self,position):
        self.position=position
        new_turtle=Turtle("circle")
        new_turtle.speed("slow")
        new_turtle.penup()
        new_turtle.color(random.choice(COLOR))
        new_turtle.setposition(self.position)
        self.Body.append(new_turtle)

    def reset(self):
        for part in self.Body:
            part.goto(1000,1000)

        self.Body.clear()
        self.create_snake()
        self.head=self.Body[0]
        self.head.color("red")
        self.head.shape("arrow")