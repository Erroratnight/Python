from screen import Bakground , Score
from paddel import Paddel , Ball
from turtle import Screen, position


#Here The Background is a Class all Methods and Attribute are Mentioned in it.
back=Bakground()
back.Boundary()
score=Score() #Score is a Class Written in screen.py

screen=Screen() #The screen is Derived from Screen Class/Package To Maintain Animation Speed and Screen Update.
screen.tracer(0)

r_paddel=Paddel((620,0))  #Its Create a Paddel on Right Side at Provided position.
l_paddel=Paddel((-620,0)) ##Its Create a Paddel on Left Side at Provided position.

ball=Ball() #Now the Ball is Created all Methods are mentioned in Ball Class


#As The Pong Game Consist of Moving Both Paddel Up and Down,
#Thus In turtle Listen is used perform the Task,
#Here Up and Down Keys are Used to Control Right Paddel and w and s keys are used for Left Paddel.
screen.listen()
screen.onkey(r_paddel.UP,"Up")
screen.onkey(r_paddel.DOWN,"Down")
screen.onkey(l_paddel.UP,"w")
screen.onkey(l_paddel.DOWN,"s")

game_is_on=True

while game_is_on:
    screen.update()
    ball.move() #The First Movement of Ball is Controled

    #Ball Bounce When it Touch Top and Bottom Boundary.
    if ball.ycor() > 320 or ball.ycor() <-320:
        ball.bounce_y()

    #Ball Bounce when its Touch/Strike The Paddles in Pong Game.
    if ball.distance(r_paddel)<40 and ball.xcor()>600 or ball.distance(l_paddel)<40 and ball.xcor()<-600:
        ball.bounce_x()

    #When The Right Paddle Misses the Ball then The Ball Will be reset and Left players Score Will be updated.
    if ball.xcor()>630:
        ball.reset_position()
        score.l_scorebord()

    #When The Left Paddle Misses the Ball then The Ball Will be reset and Pight players Score Will be updated.
    if ball.xcor()<-630:
        ball.reset_position()
        score.r_scorebord()

    
back.exit()