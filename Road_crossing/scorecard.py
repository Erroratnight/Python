from turtle import Turtle
FONT=("Courier",20,"normal") #You Can Change Font anytime

class Score(Turtle):
    def __init__(self):
        super().__init__()
        #Basic Requirement to Write Something
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level=0 #Initilizing Level 
        self.update_score()
    
    def update_score(self):
        self.level+=1 #Incrementing level When User Reached to FInish Line
        self.clear()
        # Writing Different Stuffs
        self.goto(-260,300)
        self.write("LEVEL:",align="center",font=FONT)
        self.goto(-210,300)
        self.write(self.level,align="center",font=FONT)

    def game_over(self):
        #Game Over Sequence when Player Hits the Cars
        self.goto(0,0)
        self.write("Game Over Try Again",align="center",font=FONT)
        self.goto(0,-30)
        self.write("Max Level:",align="center",font=FONT)
        self.goto(85,-30)
        self.level-=1
        self.write(self.level,align="center",font=FONT)