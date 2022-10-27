import turtle 
import pandas

screen = turtle.Screen()
screen.title("States Game")
image = "./us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("./us-states-game-start/50_states.csv")
all_states = data.state.to_list()
Guessed_states = []
while len(Guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(Guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in Guessed_states:
                missing_state.append(state)
            
            new_data = pandas.DataFrame(missing_state)
            new_data.to_csv("states_to_learn.csv")
    
        break
    if answer_state in all_states :
        Guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()    