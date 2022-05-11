#All Required Classes Imported
from turtle import Screen, distance, screensize
from turtle_control import Turtle_class , Boundary
from car_manager import Cars
from scorecard import Score
import time

#Basic Screen Element Added
screen=Screen()
screen.title("Road Crossing Game")
screen.listen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(700,700)
turtle=Turtle_class() #Created a player in turtle shape
bound=Boundary() #Finish line
car=Cars() # Cars Created
screen.onkey(turtle.move,"Up") #Key Event on which Turtle will move forward
score=Score() #Score Writting on the Screen

game_is_on=True  # Game Started Sequence
while game_is_on:
    time.sleep(0.1) 
    screen.update() #Updating Screen after each instance
    car.create_car() #Creating Numbers of Cars on Road
    car.move_car() # Moving Cars Forward in Right to Left Direction

    #Checking if Player Has reached to finish line
    if turtle.ycor()>300:
        car.levelup()
        turtle.reset()
        score.update_score()

    #Checking if Player had Accident with Cars Moving on Road
    for cars in car.all_cars:
        if cars.distance(turtle) < 25:
            score.game_over()
            game_is_on=False

screen.exitonclick()