from turtle import Turtle

#As Soon as Paddle is Called its Create a Paddle of width=20 and height=100
#Its Will be Moved to the Right/Left End as per Required Position.
#Here We have Used Super Class Thus our self will itself behave like Turtle.
class Paddel(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.color("white")
        self.shape("square") 
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(pos) 


    #As Mentioned in Previous File Up Movement is Contolled by UP Method and Down is Controlled by DOWN method.
    def UP(self):
        new_y=self.ycor()+40
        self.goto(self.xcor(),new_y)
    def DOWN(self):
        new_y=self.ycor()-40
        self.goto(self.xcor(),new_y)


#A Ball is Used for the Creation and Movement of Ball in Pong Game.
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=3
        self.y_move=3

    #move Method is place in While Loop Thus Continously it is moved on Turtle screen.
    def move(self):
        self.speed(10)
        new_x=self.xcor()+self.x_move 
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    #The Following Method is used to bounce back in screen , Here We Have Multipled -1 thus , it Will Convert 
    #Positive Integer into Negative and Vise Versa
    #Because When ball is Moving Forward on Bounce it Should come Backward and Vise Versa.
    #The Same Thing Goes for bounce in X direction.
    def bounce_y(self):
        self.y_move*=-1
    
    def bounce_x(self):
        self.x_move*=-1

    #reset Position is used Because Whenever any player Score Point then Game Should not End but again Start from origin Position.
    def reset_position(self):
        self.goto(0,0)
        self.x_move*=-1
        self.y_move*=-1
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)