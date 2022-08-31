import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
states_list = list(data.state)
screen.addshape(image)
turtle.shape(image)
guessed_states = []
while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="What's the other's state name?").title()

    if user_answer == "Exit":
        states_data_frame = pandas.DataFrame(states_list, columns=["State name"])
        states_data_frame.to_csv("states_to_learn.csv")
        break

    if user_answer in states_list:
        guessed_states.append(user_answer)
        states_list.remove(user_answer)
        new_state = turtle.Turtle()
        state_row = data[data.state == user_answer]
        x_cord = int(state_row["x"])
        y_cord = int(state_row["y"])
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(x_cord, y_cord)
        new_state.write(user_answer)
