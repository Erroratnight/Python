from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time

BACKGROUND_COLOR="black"
TITLE="Feed The Snake"
WALL_COLOR="white"
WALL_ALIGNMENT=[(270,270),(270,-270),(-270,-270),(270,270)]
WALL_HEADING=[270,180,90,180]
screen=Screen()
screen.setup(600,600)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(TITLE)
screen.tracer(0)

wall=Turtle()
wall.color(WALL_COLOR)
wall.hideturtle()
for i in range(4):
    wall.penup()
    wall.goto(WALL_ALIGNMENT[i])
    wall.pendown()
    wall.setheading(WALL_HEADING[i])
    wall.pensize(5)
    wall.forward(540)


snake=Snake()
food=Food()
game_score=Score()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on=True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    
    #Food Feeding
    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        game_score.score+=1
        game_score.update_score()

    #Collision With Wall
    if snake.head.xcor()>270 or snake.head.xcor() < -270 or snake.head.ycor() < -270 or snake.head.ycor() > 270:
        game_score.reset()
        time.sleep(0.3)
        snake.reset() 

    #Collision With Tail
    for body in snake.Body[1:]:
        if snake.head.distance(body) < 10:
            game_score.reset()
            time.sleep(0.3)
            snake.reset()
            
screen.exitonclick() 