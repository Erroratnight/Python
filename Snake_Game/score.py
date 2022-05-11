from turtle import Turtle
ALIGN="center"
FONT=("Arial", 10, "bold")

def reading():
        with open("E:\Git_hub\Snake_Game\data.txt") as file:
            return file.read()

def writing(x):
    with open("E:\Git_hub\Snake_Game\data.txt","w") as file:
        file.write(str(x))

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        A=reading()
        self.highscore=A
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        A=reading()
        self.highscore=A
        self.write(f"Score:{self.score}     High Score:{self.highscore}",False,ALIGN,FONT)

    def reset(self):
        if int(self.score) > int(self.highscore):
            writing(self.score)


        self.score=0
        self.update_score()

    
        
    # def game_over(self):
    #     self.penup()
    #     self.hideturtle()
    #     self.goto(0,0)
    #     self.color("white")
    #     self.write(f"Game Over Your Score is:{self.score}",False,ALIGN,FONT)