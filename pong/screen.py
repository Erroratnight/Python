from turtle import Turtle , Screen
#The Complete Background Class is used for Paration of Screen. 
class Bakground:
    def __init__(self):
        self.screen=Screen()
        self.screen.tracer(0)
        self.screen.title("Pong Game")
        self.screen.setup(1370,700)
        self.screen.bgcolor("black")

    def Boundary(self):
        Length=[1320,660,1320,660]
        self=Turtle()
        self.speed(0)
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.setposition(-660,-330)
        self.pendown()
        for i in range(4):
            self.forward(Length[i])
            self.left(90)

    def exit(self):
        self.screen.exitonclick()


#This Class Maintain enitre Score System.
#The Intial Constructor create a Turtle and left's and Right's Players Score.
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()

    #The Update Method Writes and Update the Score 
    #Each time its Write Score it will Clear Previous Score.
        
    def update_score(self):
        self.clear()
        self.goto(-50,250)
        self.write(self.l_score,align="center",font=("Courier",50,"normal"))
        self.goto(50,250)
        self.write(self.r_score,align="center",font=("Courier",50,"normal"))
        
    #Increment the Score for the respected players
    def l_scorebord(self):
        self.l_score+=1
        self.update_score()

    def r_scorebord(self):
        self.r_score+=1
        self.update_score()