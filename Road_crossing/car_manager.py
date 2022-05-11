from turtle import Turtle
import random

#Basics Constants which are required for cars.
SPEED=7
SPEED_INC=5
COLOR=["red","blue","white","grey","pink","brown","violet","green","sky blue","light green"]

class Cars():
    #Creating Cars and Initilizing the initial speed
    def __init__(self):
        self.all_cars=[]
        self.speed=SPEED

    def create_car(self):
        #Here if Condition is used to Slow Down the car Generation.
        car_created=random.randint(1,6)
        if car_created==1:
            #Car is Generated
            car=Turtle("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.color(random.choice(COLOR))
            random_y=random.randint(-250,250)
            car.goto(300,random_y)
            self.all_cars.append(car)

    #Car Moving Sequence 
    #Used Backward because the car heading was set to 0.
    #If you Use Forward Make Sure to set Heading as 180
    def move_car(self):
        for i in self.all_cars:
            i.backward(self.speed)
    #On levelup The Car Speed is incremented as Defined in Constant
    def levelup(self):
        self.speed+=SPEED_INC

