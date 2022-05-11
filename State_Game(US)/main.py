from turtle import Screen
import turtle
import pandas

screen=Screen()
screen.title("US Game")
image=r"E:\\Git_hub\\State_Game(US)\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

State_Data=pandas.read_csv("E:\\Git_hub\\State_Game(US)\\50_states.csv")

all_state=State_Data["state"].tolist()
gussed_list=[]
game_is_on=True
State_count=0
while State_count!=50 and game_is_on:
    State = screen.textinput(f"State:{State_count}/50","Enter Correct State name")
    State = State.capitalize()
    if State in all_state:
        gussed_list.append(State)
        turtle1=turtle.Turtle()
        turtle1.hideturtle()
        turtle1.penup()
        a_state=State_Data[State_Data.state==State]
        turtle1.goto(int(a_state.x) , int(a_state.y))
        State_count+=1
        turtle1.write(State)
    elif State=="Exit":
        game_is_on=False

to_learn_list=[]

for state in all_state:
    if state not in gussed_list:
        to_learn_list.append(state)


new_data=pandas.DataFrame(to_learn_list)
new_data.to_csv("./To_Be_Learned.csv")

