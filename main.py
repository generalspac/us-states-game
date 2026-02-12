from turtle import Turtle,Screen
import pandas as pd

#the turtle part
ecran=Screen()
ecran.title("Welcome")
writer=Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")
ecran.setup(width=725,height=491)
ecran.bgpic("blank_states_img.gif")
#the data analysis part
data=pd.read_csv("50_states.csv")
guessed_states=[] #we will add here the guessed states
state_count=0
while state_count<len(data.state):
    user_information = ecran.textinput(title="States(write Exit to leave)", prompt=f"you guessed {state_count}/{len(data.state)}").title()
    if user_information in data.state.to_list(): #we verifie if the state is in our data
        guessed_states.append(user_information)
        x_row=data[data.state==user_information]
        x_coord=x_row['x'].values[0]-20
        y_coord=x_row['y'].values[0]#we access to the first value of the numpy array
        #because when we access to a series(column),it gives us a numpy array
        #let's write with the turtle
        writer.goto(x_coord,y_coord)
        writer.pendown()
        writer.write(user_information)
        writer.penup()
        state_count+=1
        if state_count==len(data.state):
            writer.clear()
            writer.goto(0,0)
            writer.write("Congratulations!,you have guessed all the states!",align="center", font=("Arial", 24, "bold"))
    elif user_information=="Exit":
        ecran.bye()
        revision = []
        for state in data.state.to_list():
            if state not in guessed_states:
                revision.append(state)
        revision_file = pd.Series(revision)
        revision_file.to_csv("your revision sheet.csv")

ecran.exitonclick()
#let's create a file for the revision sheet
